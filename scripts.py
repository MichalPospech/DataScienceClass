import pandas as pd
import seaborn as sns
import seaborn.objects as so
import matplotlib.ticker as ticks

base_size = (7, 5)

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


def plot_gender_counts(df: pd.DataFrame):
    return _plot_dist_bar(df, ["sl11muzi", "sl11zeny"],
                          ["Men", "Women"]).label(
                              title="Number of men and women", x="Count")


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
    ).label(
        title="Percentage of inhabitants with a particular level of education",
        x=None,
    )


def plot_other_sociodem(df: pd.DataFrame):

    return _plot_dist_bar_ratio(
        df,
        ["sl11rozv", "sl11deti", "sl11seni", "sl11kat", "sl11rom"],
        ["Divorced", "Children", "Pensioners", "Catholics", "Roma"],
    ).label(
        title="Percentage of inhabitants belonging to a particular groups",
        x=None,
    ).layout(size=base_size)


def get_employment_municipality_plot(df):
    return box_cross_size_plot(
        df, "sl11obyvatel", {
            "sl11zam": "Employee",
            "sl11pod": "Enterpreneur",
            "sl11nezam": "Unemployed",
            "sl11neprduch": "Retired",
        }).label(
            x=None,
            y="Municipality size",
            title="Employment status by municipality size",
            color="Employment status",
        ).limit(x=(0, 1.0)).theme(object_theme)


def plot_municipality_size_ratio(df: pd.DataFrame):
    counts = df.groupby("vel.obce_cat")["sl11obyvatel"].sum()[[
        "500-", "500-1k", "1-5k", "5-10k", "10-20k", "20-50k", "50-100k",
        "100k+"
    ]]
    counts.index = counts.index.reorder_categories([
        "500-", "500-1k", "1-5k", "5-10k", "10-20k", "20-50k", "50-100k",
        "100k+"
    ])
    p = so.Plot(
        x=counts / df["sl11obyvatel"].sum(),
        y=counts.index,
        color=counts.index
    ).add(so.Bar(), legend=False).scale(x=so.Continuous(
    ).label(ticks.PercentFormatter(xmax=1))).label(
        title="Percentage of inhabitants living a municipality of given size",
        x=None,
        y="Size of municipality").layout(size=base_size)
    return p


def load_extended_dataset(path):
    df = pd.read_csv(path, sep=";", index_col="obec_okrsek")
    df["obec"] = df["obec"].astype(object)
    df["vel.obce_cat"] = df["vel.obce_cat"].astype("category")
    return df


def _plot_dist_bar_ratio(df, cols, names, ax=None):
    counts = df[cols].sum()
    g = so.Plot(x=counts / df["sl11obyvatel"].sum(), y=names,
                color=names).add(so.Bar(), legend=False).scale(
                    color="Paired",
                    x=so.Continuous().label(
                        ticks.PercentFormatter(xmax=1))).layout(size=base_size)
    if ax:
        g = g.on(ax)
    return g


def _plot_dist_bar(df, cols, names):
    formatter = ticks.ScalarFormatter(useOffset=False)
    formatter.set_scientific(False)
    counts = df[cols].sum()
    return so.Plot(x=counts, y=names, color=names).add(
        so.Bar(), legend=False).scale(
            color="Paired",
            x=so.Continuous().label(formatter)).layout(size=base_size)


def _plot_election_graph(df, cols, names, vote_count_col, ax=None):
    counts = df[cols].sum()[cols]
    plot = so.Plot(
        x=counts / df[vote_count_col].sum(), y=names,
        color=names).add(so.Bar(), legend=False).theme(object_theme).scale(
            color="Paired",
            x=so.Continuous().label(
                ticks.PercentFormatter(xmax=1))).layout(size=base_size)
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
            "Piráti",
            "KSČM",
            "ČSSD",
            "KDU",
            "STAN",
            "TOP09",
            "Svobodní",
            "Zelení",
        ],
        "par17phcelkem",
        ax=ax,
    ).label(
        title="Elections 2017",
        x=None,
    ).scale(color="Paired")


def plot_elections_2021(df, ax=None):
    return _plot_election_graph(
        df,
        [
            "par21ano",
            "par21spolu",
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
    ).label(title="Elections 2021", x=None).scale(color="Paired")


def plot_employment_size(df):

    return box_cross_size_plot(
        df,
        "sl11obyvatel",
        {
            "sl11zam": "Employee",
            "sl11pod": "Enterpreneur",
            "sl11nezam": "Unemployed",
            "sl11neprduch": "Retired",
        },
    ).label(
        x=None,
        y="Municipality size",
        title="Employment status by municipality size",
        color="Employment status",
    ).limit(x=(0, 1.0))


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
    plot = so.Plot(data=df, x="value", y=df.index,
                   color="variable").add(so.Bar(), so.Stack()).scale(
                       color="Paired",
                       x=so.Continuous().label(ticks.PercentFormatter(
                           xmax=1))).theme(object_theme).layout(size=base_size)

    return plot


def education_size_plot(df: pd.DataFrame):
    plot = box_cross_size_plot(
        df,
        "sl11obyvatel",
        {
            "sl11vs": "University",
            "sl11vos": "Vocational",
            "sl11nast": "Extended high",
            "sl11strm": "High w/ maturita",
            "sl11strb": "High w/o maturita",
            "sl11zakl": "Elementary",
        },
    ).label(
        x=None,
        y="Municipality size",
        title="Education by municipality size",
        color="Education",
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
            "par17ksc": "KSČM",
            "par17soc": "ČSSD",
            "par17kdu": "KDU",
            "par17sta": "STAN",
            "par17top": "Piráti",
            "par17svo": "Svobodní",
            "par17zel": "Zelení",
        },
    ).label(
        x=None,
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
            "par21pri": "Přísaha",
            "par21soc": "ČSSD",
            "par21ksc": "KSČM",
            "par21tss": "Trikolora",
            "par21zel": "Zelení",
        },
    ).label(
        x=None,
        y="Municipality size",
        title="Results by municipality size - 2021",
        color="Party",
    )


def correlations(
    df,
    rows,
    cols,
    row_trans,
    columm_trans,
):
    corr = df[rows + cols].corr().loc[rows, cols]
    renamed = corr.rename(index=row_trans).rename(columns=columm_trans)
    return renamed


def correlations_2021(df):
    rows = [
        'par21ano_ratio', 'par21spolu_ratio', 'par21spd_ratio',
        'par21pirsta_ratio', 'par21pri_ratio', 'par21soc_ratio',
        'par21ksc_ratio', 'par21zel_ratio', 'par21tss_ratio'
    ]
    cols = [
        'sl11muzi_ratio', 'sl11rozv_ratio', 'sl11deti_ratio', 'sl11seni_ratio',
        'sl11kat_ratio', 'sl11rom_ratio', 'sl11vs_ratio', 'sl11vos_ratio',
        'sl11nast_ratio', 'sl11strm_ratio', 'sl11strb_ratio', 'sl11zakl_ratio',
        'sl11zam_ratio', 'sl11pod_ratio', 'sl11nezam_ratio',
        'sl11neprduch_ratio'
    ]
    row_translate = {
        "par21spolu_ratio": "SPOLU",
        "par21ano_ratio": "ANO",
        "par21pirsta_ratio": "PirSTAN",
        "par21spd_ratio": "SPD",
        "par21pri_ratio": "Přísaha",
        "par21soc_ratio": "ČSSD",
        "par21ksc_ratio": "KSČM",
        "par21tss_ratio": "Trikolora",
        "par21zel_ratio": "Zelení",
    }
    col_translate = {
        'sl11muzi_ratio': 'Men',
        'sl11rozv_ratio': 'Divorced',
        'sl11deti_ratio': 'Children',
        'sl11seni_ratio': 'Pensioners',
        'sl11kat_ratio': 'Catholic',
        'sl11rom_ratio': 'Roma',
        'sl11vs_ratio': 'University',
        'sl11vos_ratio': 'Vocational',
        'sl11nast_ratio': 'Extended high school',
        'sl11strm_ratio': 'High school with maturita',
        'sl11strb_ratio': 'High school without maturita',
        'sl11zakl_ratio': 'Elementary school',
        'sl11zam_ratio': 'Employees',
        'sl11pod_ratio': 'Enterpreneurs',
        'sl11nezam_ratio': 'Unemployed',
        'sl11neprduch_ratio': 'Retired'
    }
    return correlations(df, rows, cols, row_translate, col_translate).T


def correlations_2017(df):
    rows = [
        'par17ano_ratio', 'par17ods_ratio', 'par17pir_ratio', 'par17spd_ratio',
        'par17ksc_ratio', 'par17soc_ratio', 'par17kdu_ratio', 'par17top_ratio',
        'par17sta_ratio', 'par17zel_ratio', 'par17svo_ratio'
    ]
    cols = [
        'sl11muzi_ratio', 'sl11rozv_ratio', 'sl11deti_ratio', 'sl11seni_ratio',
        'sl11kat_ratio', 'sl11rom_ratio', 'sl11vs_ratio', 'sl11vos_ratio',
        'sl11nast_ratio', 'sl11strm_ratio', 'sl11strb_ratio', 'sl11zakl_ratio',
        'sl11zam_ratio', 'sl11pod_ratio', 'sl11nezam_ratio',
        'sl11neprduch_ratio'
    ]
    row_translate = {
        "par17ano_ratio": "ANO",
        "par17ods_ratio": "ODS",
        "par17spd_ratio": "SPD",
        "par17pir_ratio": "TOP09",
        "par17ksc_ratio": "KSČM",
        "par17soc_ratio": "ČSSD",
        "par17kdu_ratio": "KDU",
        "par17sta_ratio": "STAN",
        "par17top_ratio": "Piráti",
        "par17svo_ratio": "Svobodní",
        "par17zel_ratio": "Zelení",
    }
    col_translate = {
        'sl11muzi_ratio': 'Men',
        'sl11rozv_ratio': 'Divorced',
        'sl11deti_ratio': 'Children',
        'sl11seni_ratio': 'Pensioners',
        'sl11kat_ratio': 'Catholic',
        'sl11rom_ratio': 'Roma',
        'sl11vs_ratio': 'University',
        'sl11vos_ratio': 'Vocational',
        'sl11nast_ratio': 'Extended high school',
        'sl11strm_ratio': 'High school with maturita',
        'sl11strb_ratio': 'High school without maturita',
        'sl11zakl_ratio': 'Elementary school',
        'sl11zam_ratio': 'Employees',
        'sl11pod_ratio': 'Enterpreneurs',
        'sl11nezam_ratio': 'Unemployed',
        'sl11neprduch_ratio': 'Retired'
    }
    return correlations(
        df,
        rows,
        cols,
        row_translate,
        col_translate,
    ).T
