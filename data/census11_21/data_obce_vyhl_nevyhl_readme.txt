1) Úvod
    Upravená data ze sèítání lidu 2011 a 2021 na úrovni obcí.
    Data by se dala rozdìlit do 11 skupin (v závorce vždy uvedeno, jak daný sloupec zaèíná):
    1) dìti (deti)
    2) domy materiál (domy_mat)
    3) domy období výstavby/rekonstrukce (domy_obd)
    4) domy vlastník (domy_vlast)
    5) mateøský jazyk (jazyk)
    6) národnost (narod)
    7) obèanství (obcanstvi)
    8) rodinný stav (rod_stav)
    9) vìk (vek) - možnost buï celkovì vìk (muži a ženy dohromady) nebo možnost podrozdìlit na pouze muže (vek_muzi) nebo pouze ženy (vek_zeny)
    10) náboženská víra (vira)
    11) vzdìlání (vzdelani)

    Poté následuje konkrétní kategorie dané skupiny, tedy napø. "deti_3" znaèí 3 dìti, "domy_vlast_byt_dr" jsou domy vlastnìné bytovým družstvem 
    Mùže následovat "_vyhl", což znamená, že je daná featura vyhlazena.
    Nakonec následuje buï
                          2011, což jsou data z roku 2011 (pokud jsme pro dané kategorie mìli data pouze z roku 2011)
                      nebo 
                          2021, což jsou data z roku 2021 (pokud jsme pro dané kategorie mìli data pouze z roku 2021)
                      nebo
                          mean - prùmìr z dat 2011 a 2021
                      nebo
                          diff - rozdíl 2021 a 2011


2) Podrobný popis sloupcù:
    OBEC_KOD - kód obce
    OBEC_NAZEV - název obce

    deti_0_2021 - bezdìtné (data z roku 2021)
    deti_1_2021 - jedno dítì (data z roku 2021)
    deti_2_2021 - dvì dìti (data z roku 2021)
    deti_3_2021 - tøi dìti (data z roku 2021)
    deti_4_2021 - ètyøi dìti (data z roku 2021)
    deti_5_vice_2021 - pìt a více dìtí (data z roku 2021)
    deti_nezj_2021  - poèet dìtí nezjištìn (data z roku 2021)

    domy_mat_drevo_2021 - domy ze døeva (data z roku 2021)
    domy_mat_kamen_cihly_2021 - domy z kamene/cihel/tvárnic (data z roku 2021)
    domy_mat_nep_cihly_2021 - domy z nepálených cihel (data z roku 2021)
    domy_mat_nezj_2021  - domy s nezjištìným materiálem (data z roku 2021)
    domy_mat_ostatni_2021 - domy z jiného materiálu (data z roku 2021)
    domy_mat_panel_2021 - domy z panelu (data z roku 2021)

    domy_obd_1919_2021 - domy z období výstavby èi rekonstrukce z roku 1919 a døíve (data z roku 2021)
    domy_obd_1920_1945_2021 - domy z období výstavby èi rekontrukce z let 1920 až 1945 (data z roku 2021)
    domy_obd_1946_1970_2021 - domy z období výstavby èi rekontrukce z let 1946 až 1970 (data z roku 2021)
    domy_obd_1971_1980_2021
    domy_obd_1981_1990_2021
    domy_obd_1991_2000_2021
    domy_obd_2001_2010_2021
    domy_obd_2011_2015_2021
    domy_obd_2016_2021 - domy z období výstavby èi rekonstrukce z roku 2016 a pozdìji (data z roku 2021)
    domy_obd_nezj_2021 - domy pro které období výstavby èi rekontrukce nebylo zjištìno (data z roku 2021)

    domy_vlast_byt_dr_mean - domy s vlatníkem bytové družstvo (prùmìr z dat 2011 a 2021)
    domy_vlast_byt_dr_diff - domy s vlastníkem bytové družstvo (hodnoty z 2021 mínus hodnoty z 2011)
    domy_vlast_fyz_mean - domy s vlastníkem fyzická osoba (prùmìr z dat 2011 a 2021)
    domy_vlast_fyz_diff
    domy_vlast_obec_stat_mean - domy s vlastníkem obec/stát (prùmìr z dat 2011 a 2021)
    domy_vlast_obec_stat_diff
    domy_vlast_spol_mean - domy s vlastníkem spoluvlastnictví vlastníkù bytù (jednotek) (prùmìr z dat 2011 a 2021) 
    domy_vlast_spol_diff

    jazyk_cesky_2021 - mateøský jazyk èeský (data z roku 2021)
    jazyk_nezj_2021 - mateøský jazyk nezjištìn (data z roku 2021)
    jazyk_slov_2021 - mateøský jazyk slovenský (data z roku 2021)
    jazyk_ukr_2021 - mateøský jazyk ukrajinský (data z roku 2021)

    narod_ceska_mean - národnost èeská (prùmìr z dat 2011 a 2021) 
    narod_ceska_diff - národnost èeská (hodnoty z 2021 mínus hodnoty z 2011)
    narod_morav_mean - národnost moravská (prùmìr z dat 2011 a 2021)
    narod_morav_diff
    narod_nezj_2011 - národnost nezjištìna (data z roku 2011)
    narod_slov_mean - národnost slovenská (prùmìr z dat 2011 a 2021) 
    narod_slov_diff
    narod_ukr_mean - národnost ukrajinská (prùmìr z dat 2011 a 2021)
    narod_ukr_diff

    obcanstvi_cesko_2021 - obèanství èeské (data z roku 2021)
    obcanstvi_nezj_2021 - obèanství nezjištìno (data z roku 2021)
    obcanstvi_slov_2021 - obèanství slovenské (data z roku 2021)
    obcanstvi_ukr_2021  - obèanství ukrajinské (data z roku 2021)

    rod_stav_nezj_2021 - rodinný stav nezjištìn (data z roku 2021)
    rod_stav_rozv_mean - rodinný stav rozvedený/rozvedená (prùmìr z dat 2011 a 2021)
    rod_stav_rozv_diff - rodinný stav rozvedený/rozvedená (hodnoty z 2021 mínus hodnoty z 2011)
    rod_stav_svob_mean - rodinný stav svobodný/svobodná (prùmìr z dat 2011 a 2021)
    rod_stav_svob_diff
    rod_stav_vdov_mean - rodinný stav vdovec/vdova (prùmìr z dat 2011 a 2021)
    rod_stav_vdov_diff
    rod_stav_zen_vdana_mean - rodinný stav ženatý/vdaná (prùmìr z dat 2011 a 2021)
    rod_stav_zen_vdana_diff

    vek_0_14_mean - vìk 0 až 14 (prùmìr z dat 2011 a 2021)
    vek_0_14_diff - vìk 0 až 14 (hodnoty z 2021 mínus hodnoty z 2011)
    vek_15_19_mean - vìk 15 až 19 (prùmìr z dat 2011 a 2021)
    vek_15_19_diff
    vek_20_29_mean
    vek_20_29_diff
    vek_30_39_mean
    vek_30_39_diff
    vek_40_49_mean
    vek_40_49_diff
    vek_50_59_mean
    vek_50_59_diff
    vek_60_64_mean
    vek_60_64_diff
    vek_65_69_mean
    vek_65_69_diff
    vek_70_79_mean
    vek_70_79_diff
    vek_80_inf_mean - vìk 80 a více (prùmìr z dat 2011 a 2021) 
    vek_80_inf_diff - vìk 80 a více (hodnoty z 2021 mínus hodnoty z 2011)
    vek_muzi_0_14_mean - muži ve vìku 0 až 14  (prùmìr z dat 2011 a 2021)
    vek_muzi_0_14_diff - muži ve vìku 0 až 14 (hodnoty z 2021 mínus hodnoty z 2011)
    vek_muzi_15_19_mean
    vek_muzi_15_19_diff
    vek_muzi_20_29_mean
    vek_muzi_20_29_diff
    vek_muzi_30_39_mean
    vek_muzi_30_39_diff
    vek_muzi_40_49_mean
    vek_muzi_40_49_diff
    vek_muzi_50_59_mean
    vek_muzi_50_59_diff
    vek_muzi_60_64_mean
    vek_muzi_60_64_diff
    vek_muzi_65_69_mean
    vek_muzi_65_69_diff
    vek_muzi_70_79_mean
    vek_muzi_70_79_diff
    vek_muzi_80_inf_mean
    vek_muzi_80_inf_diff
    vek_zeny_0_14_mean - ženy ve vìku 0 až 14 (prùmìr z dat 2011 a 2021)
    vek_zeny_0_14_diff - ženy ve vìku 0 až 14 (hodnoty z 2021 mínus hodnoty z 2011)
    vek_zeny_15_19_mean
    vek_zeny_15_19_diff
    vek_zeny_20_29_mean
    vek_zeny_20_29_diff
    vek_zeny_30_39_mean
    vek_zeny_30_39_diff
    vek_zeny_40_49_mean
    vek_zeny_40_49_diff
    vek_zeny_50_59_mean
    vek_zeny_50_59_diff
    vek_zeny_60_64_mean
    vek_zeny_60_64_diff
    vek_zeny_65_69_mean
    vek_zeny_65_69_diff
    vek_zeny_70_79_mean
    vek_zeny_70_79_diff
    vek_zeny_80_inf_mean
    vek_zeny_80_inf_diff

    vira_ateisti_mean - bez náboženské víry (prùmìr z dat 2011 a 2021)
    vira_ateisti_diff - bez náboženské víry (hodnoty z 2021 mínus hodnoty z 2011)
    vira_evangelici_mean - Èeskobratrská církev evangelická (prùmìr z dat 2011 a 2021)
    vira_evangelici_diff
    vira_hlasici_mean - vìøící hlásící se k církvi nebo náboženské spoleènosti (prùmìr z dat 2011 a 2021)
    vira_hlasici_diff
    vira_husiti_mean - Církev èeskoslovenská husitská (prùmìr z dat 2011 a 2021)
    vira_husiti_diff 
    vira_katolici_mean - Církev øímskokatolická (prùmìr z dat 2011 a 2021)
    vira_katolici_diff
    vira_nehlasici_mean - vìøící, ale nehlásící se k žádné církvi ani náboženské spoleènosti (prùmìr z dat 2011 a 2021)
    vira_nehlasici_diff
    vira_nezj_mean - víra nezjištìna (prùmìr z dat 2011 a 2021)
    vira_nezj_diff

    vzdelani_bez_mean - bez vzdìlání (prùmìr z dat 2011 a 2021)
    vzdelani_bez_diff - bez vzdìlání (hodnoty z 2021 mínus hodnoty z 2011)
    vzdelani_nezj_2021 - vzdìlání nezjištìno (data z roku 2021)
    vzdelani_str_bm_mean - vzdìlání støední vè. vyuèení (bez maturity)  (prùmìr z dat 2011 a 2021)
    vzdelani_str_bm_diff
    vzdelani_str_np_mean - vzdìlání støední (s maturitou), vè. nástavbového a pomaturitního (prùmìr z dat 2011 a 2021)
    vzdelani_str_np_diff
    vzdelani_vo_mean - vzdìlání vyšší odborné/konzervatoø (prùmìr z dat 2011 a 2021)
    vzdelani_vo_diff
    vzdelani_vys_mean - vzdìlání vysokoškolské (prùmìr z dat 2011 a 2021)
    vzdelani_vys_diff
    vzdelani_zakl_mean - vzdìlání základní vè. neukonèeného (prùmìr z dat 2011 a 2021)
    vzdelani_zakl_diff

    vzdelani_nezj_vyhl_2021 - vyhlazená featura vzdelani_nezj_2021
    jazyk_nezj_vyhl_2021 - vyhlazená featura jazyk_nezj_2021
    jazyk_cesky_vyhl_2021 - vyhlazená featura jazyk_cesky_2021
    deti_5_vice_vyhl_2021 - vyhlazená featura deti_5_vice_2021
    domy_obd_1919_vyhl_2021 - vyhlazená featura domy_obd_1919_2021
    rod_stav_rozv_vyhl_mean - vyhlazená featura rod_stav_rozv_mean
    vzdelani_zakl_vyhl_mean - vyhlazená featura vzdelani_zakl_mean
    rod_stav_zen_vdana_vyhl_mean - vyhlazená featura rod_stav_zen_vdana_mean
    vzdelani_str_np_vyhl_mean - vyhlazená featura vzdelani_str_np_mean
    vzdelani_vys_vyhl_mean - vyhlazená featura vzdelani_vys_mean
    vira_ateisti_vyhl_mean - vyhlazená featura vira_ateisti_mean
    vek_80_inf_vyhl_mean - vyhlazená featura vek_80_inf_mean
    domy_vlast_obec_stat_vyhl_mean - vyhlazená featura domy_vlast_obec_stat_mean
    domy_vlast_fyz_vyhl_mean - vyhlazená featura domy_vlast_fyz_mean



3) Více detailù - jak jsme k hodnotám dospìli:
     Nejprve jsme napoèítali pomìry pro všechny obce a všechny kategorie, tedy napø. jsme si vzali danou obec, podívali jsme se kolik v ní žije lidí ve vìku 0-14 a toto èíslo jsme
     vydìlili poètem lidí v obci.
     Vzdìlání je poèítáno ku poètu obyvatel 15+.
     Poèet dìtí je poèítán ku poètu žen 15+.
     Pokud jsme mìli pro urèité kategorie hodnoty pro roky 2011 i 2021, tak jsme spoèítali prùmìr tìchto hodnot (mean) a rozdíl tìchto hodnot (diff).
     Featury, které se zdály být nejlepší, jsme ještì vyhladili pomocí beta rozdìlení (vyhl v názvu).
     
    
