import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn.objects as so

theme = {
    "context": "notebook",
    "style": "darkgrid",
    "palette": "Paired",
    "font": "sans-serif",
    "font_scale": 1,
    "color_codes": True,
    "rc": None,
}

object_theme = {
    **sns.axes_style("darkgrid"),
    **sns.plotting_context("notebook")
}
sns.set_palette("Paired")
sns.set_theme(**theme)


def plot_gender_counts(df: pd.DataFrame):
    return _plot_dist_bar(
        df, ["sl11muzi", "sl11zeny"],
        ["Men", "Women"]).label(title="Number of men and women")


def plot_edu_count(df: pd.DataFrame):
    return _plot_dist_bar_ratio(
        df,
        ["sl11vs", "sl11vos", "sl11nast", "sl11strm", "sl11strb", "sl11zakl"],
        [
            "University",
            "Vocational",
            "Extended high",
            "High w/ m.",
            "High w/o m.",
            "Elementary",
        ],
    ).label(title="Ratio of inhabitants with a particular level of education")


def plot_municipality_size_ratio(df: pd.DataFrame):
    counts = df.groupby("vel.obce_cat")["sl11obyvatel"].sum()[[
        "500-", "500-1k", "1-5k", "5-10k", "10-20k", "20-50k", "50-100k",
        "100k+"
    ]]
    return so.Plot(x=counts / df["sl11obyvatel"].sum(), y=counts.index, color =counts.index).add(so.Bar()).label(
       title="Ratio of inhabitants living a municipality of given size",
       x= "Number of inhabitants",
       y="Size of municipality"

    )

def load_extended_dataset(path):
    df = pd.read_csv(path, sep=";", index_col="obec_okrsek")
    df["obec"] = df["obec"].astype(object)
    df["vel.obce_cat"] = df["vel.obce_cat"].astype("category")
    return df


def _plot_dist_bar_ratio(df, cols, names, ax=None):
    counts = df[cols].sum()
    g = so.Plot(x=counts / df["sl11obyvatel"].sum(), y=names, color=names).add(so.Bar()).scale(color="Paired")
    if ax:
        g = g.on(ax)
    return g


def _plot_dist_bar(df, cols, names):
    counts = df[cols].sum()
    return so.Plot(x=counts, y=names, color=names).add(so.Bar()).scale(color="Paired")


def _plot_election_graph(df, cols, names, vote_count_col, ax=None):
    counts = df[cols].sum()[cols]
    plot =  so.Plot(x=counts / df[vote_count_col].sum(), y=names, color=names).add(so.Bar()).theme(object_theme).scale(color="Paired")
    if ax:
        plot = plot.on(ax)
    return plot



def plot_elections_2017(df, ax=None):
    return _plot_election_graph(
        df,
        [
            "par17ano",
            "par17ods",
            "par17spd",
            "par17pir",
            "par17ksc",
            "par17soc",
            "par17kdu",
            "par17sta",
            "par17top",
            "par17svo",
            "par17zel",
        ],
        [
            "ANO",
            "ODS",
            "SPD",
            "TOP09",
            "KSCM",
            "CSSD",
            "KDU",
            "STAN",
            "Pirati",
            "Svobodni",
            "Zeleni",
        ],
        "par17phcelkem",
        ax=ax,
    ).label(title="Elections 2017").scale(color="Paired")


def plot_elections_2021(df, ax=None):
    return _plot_election_graph(
        df,
        [
            "par21spolu",
            "par21ano",
            "par21pirsta",
            "par21spd",
            "par21pri",
            "par21soc",
            "par21ksc",
            "par21tss",
            "par21zel",
        ],
        [
            "ANO",
            "SPOLU",
            "PirSTAN",
            "SPD",
            "Přísaha",
            "ČSSD",
            "KSČM",
            "Trikolora",
            "Zelení",
        ],
        "par21phcelkem",
        ax=ax,
    ).label(title="Elections 2021").scale(color="Paired")


def plot_employment_size(df):

    return (box_cross_size_plot(
        df,
        "sl11obyvatel",
        {
            "sl11zam": "Employee",
            "sl11pod": "Enterpreneur",
            "sl11nezam": "Unemployed",
            "sl11neprduch": "Retired",
        },
    ).label(
        x="Ratio",
        y="Municipality size",
        title="Employment status by municipality size",
        color="Employment status",
    ).limit(x=(0, 1.0)))


def box_cross_size_plot(df: pd.DataFrame, base_col, translation):
    df = df.groupby("vel.obce_cat")[list(translation.keys()) +
                                    [base_col]].sum()
    for col in df.columns:
        if col != base_col:
            df[col] = df[col] / df[base_col]
    df = df.drop([base_col], axis=1)
    df = df.melt(ignore_index=False)
    df["variable"] = df["variable"].apply(lambda x: translation[x])

    df.index = df.index.reorder_categories([
        "500-", "500-1k", "1-5k", "5-10k", "10-20k", "20-50k", "50-100k",
        "100k+"
    ])
    plot = (so.Plot(data=df, x="value", y=df.index, color="variable").add(
        so.Bar(), so.Stack()).scale(color="Paired")).theme(object_theme)

    return plot


def education_size_plot(df: pd.DataFrame):
    plot = box_cross_size_plot(
        df,
        "sl11obyvatel",
        {
            "sl11vs": "University",
            "sl11vos": "Vocational",
            "sl11nast": "Extended high",
            "sl11strm": "High w/ m.",
            "sl11strb": "High w/o m.",
            "sl11zakl": "Elementary",
        },
    ).label(
        x="Ratio",
        y="Municipality size",
        title="Results by municipality size",
        color="Party",
    )

    return plot


def elections2017_size_plot(df: pd.DataFrame):
    return box_cross_size_plot(
        df,
        "par17phcelkem",
        {
            "par17ano": "ANO",
            "par17ods": "ODS",
            "par17spd": "SPD",
            "par17pir": "TOP09",
            "par17ksc": "KSCM",
            "par17soc": "CSSD",
            "par17kdu": "KDU",
            "par17sta": "STAN",
            "par17top": "Pirati",
            "par17svo": "Svobodni",
            "par17zel": "Zeleni",
        },
    ).label(
        x="Ratio",
        y="Municipality size",
        title="Results by municipality size - 2017",
        color="Party",
    )


def elections2021_size_plot(df: pd.DataFrame):
    return box_cross_size_plot(
        df,
        "par21phcelkem",
        {
            "par21spolu": "SPOLU",
            "par21ano": "ANO",
            "par21pirsta": "PirSTAN",
            "par21spd": "SPD",
            "par21pri": "Prisaha",
            "par21soc": "CSSD",
            "par21ksc": "KSCM",
            "par21tss": "Trikolor",
            "par21zel": "Zeleni",
        },
    ).label(
        x="Ratio",
        y="Municipality size",
        title="Results by municipality size - 2021",
        color="Party",
    )


def create_jointplot(df, x, y, labels):

    fig, axes = plt.subplots(ncols=len(x),
                             nrows=len(y),
                             figsize=(len(x) * 8, len(y) * 6))
    for i in range(len(x)):
        for j in range(len(y)):
            (so.Plot(df, x=x[i], y=y[j]).add(so.Dots(pointsize=1)).on(
                axes[i][j]).theme(object_theme).label(**labels[i][j]).plot())
    fig.suptitle("Relation of X and Y")
    return fig, axes
