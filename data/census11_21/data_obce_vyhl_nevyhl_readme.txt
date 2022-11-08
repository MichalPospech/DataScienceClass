1) �vod
    Upraven� data ze s��t�n� lidu 2011 a 2021 na �rovni obc�.
    Data by se dala rozd�lit do 11 skupin (v z�vorce v�dy uvedeno, jak dan� sloupec za��n�):
    1) d�ti (deti)
    2) domy materi�l (domy_mat)
    3) domy obdob� v�stavby/rekonstrukce (domy_obd)
    4) domy vlastn�k (domy_vlast)
    5) mate�sk� jazyk (jazyk)
    6) n�rodnost (narod)
    7) ob�anstv� (obcanstvi)
    8) rodinn� stav (rod_stav)
    9) v�k (vek) - mo�nost bu� celkov� v�k (mu�i a �eny dohromady) nebo mo�nost podrozd�lit na pouze mu�e (vek_muzi) nebo pouze �eny (vek_zeny)
    10) n�bo�ensk� v�ra (vira)
    11) vzd�l�n� (vzdelani)

    Pot� n�sleduje konkr�tn� kategorie dan� skupiny, tedy nap�. "deti_3" zna�� 3 d�ti, "domy_vlast_byt_dr" jsou domy vlastn�n� bytov�m dru�stvem 
    M��e n�sledovat "_vyhl", co� znamen�, �e je dan� featura vyhlazena.
    Nakonec n�sleduje bu�
                          2011, co� jsou data z roku 2011 (pokud jsme pro dan� kategorie m�li data pouze z roku 2011)
                      nebo 
                          2021, co� jsou data z roku 2021 (pokud jsme pro dan� kategorie m�li data pouze z roku 2021)
                      nebo
                          mean - pr�m�r z dat 2011 a 2021
                      nebo
                          diff - rozd�l 2021 a 2011


2) Podrobn� popis sloupc�:
    OBEC_KOD - k�d obce
    OBEC_NAZEV - n�zev obce

    deti_0_2021 - bezd�tn� (data z roku 2021)
    deti_1_2021 - jedno d�t� (data z roku 2021)
    deti_2_2021 - dv� d�ti (data z roku 2021)
    deti_3_2021 - t�i d�ti (data z roku 2021)
    deti_4_2021 - �ty�i d�ti (data z roku 2021)
    deti_5_vice_2021 - p�t a v�ce d�t� (data z roku 2021)
    deti_nezj_2021  - po�et d�t� nezji�t�n (data z roku 2021)

    domy_mat_drevo_2021 - domy ze d�eva (data z roku 2021)
    domy_mat_kamen_cihly_2021 - domy z kamene/cihel/tv�rnic (data z roku 2021)
    domy_mat_nep_cihly_2021 - domy z nep�len�ch cihel (data z roku 2021)
    domy_mat_nezj_2021  - domy s nezji�t�n�m materi�lem (data z roku 2021)
    domy_mat_ostatni_2021 - domy z jin�ho materi�lu (data z roku 2021)
    domy_mat_panel_2021 - domy z panelu (data z roku 2021)

    domy_obd_1919_2021 - domy z obdob� v�stavby �i rekonstrukce z roku 1919 a d��ve (data z roku 2021)
    domy_obd_1920_1945_2021 - domy z obdob� v�stavby �i rekontrukce z let 1920 a� 1945 (data z roku 2021)
    domy_obd_1946_1970_2021 - domy z obdob� v�stavby �i rekontrukce z let 1946 a� 1970 (data z roku 2021)
    domy_obd_1971_1980_2021
    domy_obd_1981_1990_2021
    domy_obd_1991_2000_2021
    domy_obd_2001_2010_2021
    domy_obd_2011_2015_2021
    domy_obd_2016_2021 - domy z obdob� v�stavby �i rekonstrukce z roku 2016 a pozd�ji (data z roku 2021)
    domy_obd_nezj_2021 - domy pro kter� obdob� v�stavby �i rekontrukce nebylo zji�t�no (data z roku 2021)

    domy_vlast_byt_dr_mean - domy s vlatn�kem bytov� dru�stvo (pr�m�r z dat 2011 a 2021)
    domy_vlast_byt_dr_diff - domy s vlastn�kem bytov� dru�stvo (hodnoty z 2021 m�nus hodnoty z 2011)
    domy_vlast_fyz_mean - domy s vlastn�kem fyzick� osoba (pr�m�r z dat 2011 a 2021)
    domy_vlast_fyz_diff
    domy_vlast_obec_stat_mean - domy s vlastn�kem obec/st�t (pr�m�r z dat 2011 a 2021)
    domy_vlast_obec_stat_diff
    domy_vlast_spol_mean - domy s vlastn�kem spoluvlastnictv� vlastn�k� byt� (jednotek) (pr�m�r z dat 2011 a 2021) 
    domy_vlast_spol_diff

    jazyk_cesky_2021 - mate�sk� jazyk �esk� (data z roku 2021)
    jazyk_nezj_2021 - mate�sk� jazyk nezji�t�n (data z roku 2021)
    jazyk_slov_2021 - mate�sk� jazyk slovensk� (data z roku 2021)
    jazyk_ukr_2021 - mate�sk� jazyk ukrajinsk� (data z roku 2021)

    narod_ceska_mean - n�rodnost �esk� (pr�m�r z dat 2011 a 2021) 
    narod_ceska_diff - n�rodnost �esk� (hodnoty z 2021 m�nus hodnoty z 2011)
    narod_morav_mean - n�rodnost moravsk� (pr�m�r z dat 2011 a 2021)
    narod_morav_diff
    narod_nezj_2011 - n�rodnost nezji�t�na (data z roku 2011)
    narod_slov_mean - n�rodnost slovensk� (pr�m�r z dat 2011 a 2021) 
    narod_slov_diff
    narod_ukr_mean - n�rodnost ukrajinsk� (pr�m�r z dat 2011 a 2021)
    narod_ukr_diff

    obcanstvi_cesko_2021 - ob�anstv� �esk� (data z roku 2021)
    obcanstvi_nezj_2021 - ob�anstv� nezji�t�no (data z roku 2021)
    obcanstvi_slov_2021 - ob�anstv� slovensk� (data z roku 2021)
    obcanstvi_ukr_2021  - ob�anstv� ukrajinsk� (data z roku 2021)

    rod_stav_nezj_2021 - rodinn� stav nezji�t�n (data z roku 2021)
    rod_stav_rozv_mean - rodinn� stav rozveden�/rozveden� (pr�m�r z dat 2011 a 2021)
    rod_stav_rozv_diff - rodinn� stav rozveden�/rozveden� (hodnoty z 2021 m�nus hodnoty z 2011)
    rod_stav_svob_mean - rodinn� stav svobodn�/svobodn� (pr�m�r z dat 2011 a 2021)
    rod_stav_svob_diff
    rod_stav_vdov_mean - rodinn� stav vdovec/vdova (pr�m�r z dat 2011 a 2021)
    rod_stav_vdov_diff
    rod_stav_zen_vdana_mean - rodinn� stav �enat�/vdan� (pr�m�r z dat 2011 a 2021)
    rod_stav_zen_vdana_diff

    vek_0_14_mean - v�k 0 a� 14 (pr�m�r z dat 2011 a 2021)
    vek_0_14_diff - v�k 0 a� 14 (hodnoty z 2021 m�nus hodnoty z 2011)
    vek_15_19_mean - v�k 15 a� 19 (pr�m�r z dat 2011 a 2021)
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
    vek_80_inf_mean - v�k 80 a v�ce (pr�m�r z dat 2011 a 2021) 
    vek_80_inf_diff - v�k 80 a v�ce (hodnoty z 2021 m�nus hodnoty z 2011)
    vek_muzi_0_14_mean - mu�i ve v�ku 0 a� 14  (pr�m�r z dat 2011 a 2021)
    vek_muzi_0_14_diff - mu�i ve v�ku 0 a� 14 (hodnoty z 2021 m�nus hodnoty z 2011)
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
    vek_zeny_0_14_mean - �eny ve v�ku 0 a� 14 (pr�m�r z dat 2011 a 2021)
    vek_zeny_0_14_diff - �eny ve v�ku 0 a� 14 (hodnoty z 2021 m�nus hodnoty z 2011)
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

    vira_ateisti_mean - bez n�bo�ensk� v�ry (pr�m�r z dat 2011 a 2021)
    vira_ateisti_diff - bez n�bo�ensk� v�ry (hodnoty z 2021 m�nus hodnoty z 2011)
    vira_evangelici_mean - �eskobratrsk� c�rkev evangelick� (pr�m�r z dat 2011 a 2021)
    vira_evangelici_diff
    vira_hlasici_mean - v���c� hl�s�c� se k c�rkvi nebo n�bo�ensk� spole�nosti (pr�m�r z dat 2011 a 2021)
    vira_hlasici_diff
    vira_husiti_mean - C�rkev �eskoslovensk� husitsk� (pr�m�r z dat 2011 a 2021)
    vira_husiti_diff 
    vira_katolici_mean - C�rkev ��mskokatolick� (pr�m�r z dat 2011 a 2021)
    vira_katolici_diff
    vira_nehlasici_mean - v���c�, ale nehl�s�c� se k ��dn� c�rkvi ani n�bo�ensk� spole�nosti (pr�m�r z dat 2011 a 2021)
    vira_nehlasici_diff
    vira_nezj_mean - v�ra nezji�t�na (pr�m�r z dat 2011 a 2021)
    vira_nezj_diff

    vzdelani_bez_mean - bez vzd�l�n� (pr�m�r z dat 2011 a 2021)
    vzdelani_bez_diff - bez vzd�l�n� (hodnoty z 2021 m�nus hodnoty z 2011)
    vzdelani_nezj_2021 - vzd�l�n� nezji�t�no (data z roku 2021)
    vzdelani_str_bm_mean - vzd�l�n� st�edn� v�. vyu�en� (bez maturity)  (pr�m�r z dat 2011 a 2021)
    vzdelani_str_bm_diff
    vzdelani_str_np_mean - vzd�l�n� st�edn� (s maturitou), v�. n�stavbov�ho a pomaturitn�ho (pr�m�r z dat 2011 a 2021)
    vzdelani_str_np_diff
    vzdelani_vo_mean - vzd�l�n� vy��� odborn�/konzervato� (pr�m�r z dat 2011 a 2021)
    vzdelani_vo_diff
    vzdelani_vys_mean - vzd�l�n� vysoko�kolsk� (pr�m�r z dat 2011 a 2021)
    vzdelani_vys_diff
    vzdelani_zakl_mean - vzd�l�n� z�kladn� v�. neukon�en�ho (pr�m�r z dat 2011 a 2021)
    vzdelani_zakl_diff

    vzdelani_nezj_vyhl_2021 - vyhlazen� featura vzdelani_nezj_2021
    jazyk_nezj_vyhl_2021 - vyhlazen� featura jazyk_nezj_2021
    jazyk_cesky_vyhl_2021 - vyhlazen� featura jazyk_cesky_2021
    deti_5_vice_vyhl_2021 - vyhlazen� featura deti_5_vice_2021
    domy_obd_1919_vyhl_2021 - vyhlazen� featura domy_obd_1919_2021
    rod_stav_rozv_vyhl_mean - vyhlazen� featura rod_stav_rozv_mean
    vzdelani_zakl_vyhl_mean - vyhlazen� featura vzdelani_zakl_mean
    rod_stav_zen_vdana_vyhl_mean - vyhlazen� featura rod_stav_zen_vdana_mean
    vzdelani_str_np_vyhl_mean - vyhlazen� featura vzdelani_str_np_mean
    vzdelani_vys_vyhl_mean - vyhlazen� featura vzdelani_vys_mean
    vira_ateisti_vyhl_mean - vyhlazen� featura vira_ateisti_mean
    vek_80_inf_vyhl_mean - vyhlazen� featura vek_80_inf_mean
    domy_vlast_obec_stat_vyhl_mean - vyhlazen� featura domy_vlast_obec_stat_mean
    domy_vlast_fyz_vyhl_mean - vyhlazen� featura domy_vlast_fyz_mean



3) V�ce detail� - jak jsme k hodnot�m dosp�li:
     Nejprve jsme napo��tali pom�ry pro v�echny obce a v�echny kategorie, tedy nap�. jsme si vzali danou obec, pod�vali jsme se kolik v n� �ije lid� ve v�ku 0-14 a toto ��slo jsme
     vyd�lili po�tem lid� v obci.
     Vzd�l�n� je po��t�no ku po�tu obyvatel 15+.
     Po�et d�t� je po��t�n ku po�tu �en 15+.
     Pokud jsme m�li pro ur�it� kategorie hodnoty pro roky 2011 i 2021, tak jsme spo��tali pr�m�r t�chto hodnot (mean) a rozd�l t�chto hodnot (diff).
     Featury, kter� se zd�ly b�t nejlep��, jsme je�t� vyhladili pomoc� beta rozd�len� (vyhl v n�zvu).
     
    
