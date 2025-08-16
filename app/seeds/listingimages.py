from app.models import db, Listingimage, environment, SCHEMA
from sqlalchemy.sql import text


def seed_listingimages():

    Listingimages = [
        # Listing 1 - Tripod Manfrotto (owner_id 1)
        Listingimage(listing_id = 1, listing_img = 'https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153679/TriPod3_kqdwpb.jpg'),
        Listingimage(listing_id = 1, listing_img = 'https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153680/TriPod1_mtyx2a.jpg'),
        Listingimage(listing_id = 1, listing_img = 'https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153677/TriPod6_tem1fl.jpg'),
        Listingimage(listing_id = 1, listing_img = 'https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153674/TriPod5_vwcdlt.jpg'),
        Listingimage(listing_id = 1, listing_img = 'https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153673/TriPod4_bywy7f.jpg'),

        # Listing 2 - Pro Gear Toolbox (owner_id 1)
        Listingimage(listing_id=2, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153671/IMG_2618_kgt3nn.jpg'),
        Listingimage(listing_id=2, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153670/IMG_2615_uivcah.jpg'),
        Listingimage(listing_id=2, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153672/IMG_2619_ox3alu.jpg'),
        Listingimage(listing_id=2, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153667/IMG_2617_tby4cv.jpg'),

        # Listing 3 - TLC TV 32in (owner_id 1)
        Listingimage(listing_id=3, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153665/TCLTv2_efaxfl.jpg'),
        Listingimage(listing_id=3, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153664/TCLTv1_quvcbr.jpg'),
        Listingimage(listing_id=3, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153666/TCLTv3_qazwzz.jpg'),
        Listingimage(listing_id=3, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153663/TCLTv5_gavodx.jpg'),

        # Listing 4 - Surge Protective Device (owner_id 1)
        Listingimage(listing_id=4, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153656/SurgeProtector3_siqjxi.jpg'),
        Listingimage(listing_id=4, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153661/SurgeProtector4_uodebg.jpg'),
        Listingimage(listing_id=4, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153658/SurgeProtector6_k9vb3p.jpg'),
        Listingimage(listing_id=4, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153654/SurgeProtector1_entseg.jpg'),

        # Listing 5 - Specialized Bike (owner_id 2)
        Listingimage(listing_id=5, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153649/CrassTrailBike1_ryt4no.jpg'),
        Listingimage(listing_id=5, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153651/CrassTrailBike4_shgbsm.jpg'),
        Listingimage(listing_id=5, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153650/CrassTrailBike5_o6hsfv.jpg'),
        Listingimage(listing_id=5, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153646/CrassTrailBike3_voi56o.jpg'),

        # Listing 6 - Saw Milwaukee (owner_id 2)
        Listingimage(listing_id=6, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153637/Saw1_eknru3.jpg'),
        Listingimage(listing_id=6, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153634/Saw2_ukqsyc.jpg'),
        Listingimage(listing_id=6, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153638/Saw4_aa0hgg.jpg'),
        Listingimage(listing_id=6, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153639/Saw5_hovo7h.jpg'),

        # Listing 7 - Samsung Stove (owner_id 2)
        Listingimage(listing_id=7, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153633/SamsungStove1_j4b4h1.jpg'),
        Listingimage(listing_id=7, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153631/SamsungStove3_zy9ugo.jpg'),
        Listingimage(listing_id=7, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153632/SamsungStove2_a12uli.jpg'),
        Listingimage(listing_id=7, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153630/SamsungStove4_trh3hv.jpg'),

        # Listing 8 - Samsung Microwave (owner_id 2)
        Listingimage(listing_id=8, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153629/SamsungMicro4_i0ppxm.jpg'),
        Listingimage(listing_id=8, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153626/SamsungMicro2_xtome6.jpg'),
        Listingimage(listing_id=8, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153625/SamsungMicro3_p4aogh.jpg'),
        Listingimage(listing_id=8, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153627/SamsungMicro1_oitr4d.jpg'),

        # Listing 9 - Ryobi Drill (owner_id 3)
        Listingimage(listing_id=9, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153621/RyobiDrill1_rompmo.jpg'),
        Listingimage(listing_id=9, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153618/RyobiDrill7_s1mthc.jpg'),
        Listingimage(listing_id=9, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153617/RyobiDrill6_dwokoy.jpg'),
        Listingimage(listing_id=9, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153624/RyobiDrill2_fuaqu0.jpg'),

        # Listing 10 - Ray-Ban Glasses (owner_id 3)
        Listingimage(listing_id=10, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153614/RayBans4_sdfvbx.jpg'),
        Listingimage(listing_id=10, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153615/RayBans5_azl5j4.jpg'),
        Listingimage(listing_id=10, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153612/RayBans3_xaeytu.jpg'),
        Listingimage(listing_id=10, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153611/RayBans2_metphb.jpg'),

        # Listing 11 - Hand-Held Test Kit (owner_id 3)
        Listingimage(listing_id=11, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153609/MasterPacTester6_go24je.png'),
        Listingimage(listing_id=11, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153603/MasterPacTester2_cxybas.jpg'),
        Listingimage(listing_id=11, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153604/MasterPacTester3_nsqm9v.jpg'),
        Listingimage(listing_id=11, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153607/MasterPacTester5_yckxxy.jpg'),

        # Listing 12 - Bell & Gossett Seal Kit (owner_id 3)
        Listingimage(listing_id=12, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755309490/PipeGasket3_swi3e1.jpg'),
        Listingimage(listing_id=12, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755309485/PipeGasket5_g59a9q.jpg'),
        Listingimage(listing_id=12, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755309488/PipeGasket4_xaymyb.jpg'),
        Listingimage(listing_id=12, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755309480/PipeGasket_zosza8.jpg'),

        # Listing 13 - Milwaukee Nailer (owner_id 4)
        Listingimage(listing_id=13, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153594/Nailer1_bokvnn.jpg'),
        Listingimage(listing_id=13, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153595/Nailer3_bbphfo.jpg'),
        Listingimage(listing_id=13, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153593/Nailer4_kvs8xv.jpg'),
        Listingimage(listing_id=13, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153590/Nailer6_tul81w.jpg'),

        # Listing 14 - Milwaukee Battery 2.0 Amp (owner_id 4)
        Listingimage(listing_id=14, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153588/MilwaukeeBattery5_hsdcdz.jpg'),
        Listingimage(listing_id=14, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153587/MilwaukeeBattery2_tjma7l.jpg'),
        Listingimage(listing_id=14, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153586/MilwaukeeBattery3_noucy7.jpg'),
        Listingimage(listing_id=14, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153589/MilwaukeeBattery4_pwe5eq.jpg'),

        # Listing 15 - Medical Scissors (owner_id 4)
        Listingimage(listing_id=15, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153582/Raptors3_fhtwhs.jpg'),
        Listingimage(listing_id=15, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153581/Raptors2_zhw4yu.jpg'),
        Listingimage(listing_id=15, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153583/Raptors1_ebp98v.jpg'),
        Listingimage(listing_id=15, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153578/Raptors4_f7zypz.jpg'),

        # Listing 16 - Milwaukee Impact Drill (owner_id 4)
        Listingimage(listing_id=16, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153566/MilwaukeeImpact6_yiswud.jpg'),
        Listingimage(listing_id=16, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153569/MilwaukeeImpact1_hnnvww.jpg'),
        Listingimage(listing_id=16, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153568/MilwaukeeImpact2_ut6v2v.jpg'),
        Listingimage(listing_id=16, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153563/MilwaukeeImpact5_cqyft4.jpg'),

        # Listing 17 - KitchenAid Mixer (owner_id 5)
        Listingimage(listing_id=17, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755298181/KitchenAidMixer2_jtti3p.jpg'),
        Listingimage(listing_id=17, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153575/KitchenAidMixer5_gnliec.jpg'),
        Listingimage(listing_id=17, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153576/KitchenAidMixer7_dfmcil.jpg'),
        Listingimage(listing_id=17, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153577/KitchenAidMixer6_zxow9h.jpg'),

        # Listing 18 - Milwaukee Impact Drill (owner_id 5)
        Listingimage(listing_id=18, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153569/MilwaukeeImpact1_hnnvww.jpg'),
        Listingimage(listing_id=18, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153568/MilwaukeeImpact2_ut6v2v.jpg'),
        Listingimage(listing_id=18, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153565/MilwaukeeImpact4_gxrzin.jpg'),
        Listingimage(listing_id=18, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153563/MilwaukeeImpact5_cqyft4.jpg'),

        # Listing 19 - DRD2M Light (owner_id 5)
        Listingimage(listing_id=19, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153562/DR2MLights1_jiegca.jpg'),
        Listingimage(listing_id=19, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755298361/DR2MLights5_zkku2a.jpg'),
        Listingimage(listing_id=19, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153559/DR2MLights6_mwjki8.jpg'),
        Listingimage(listing_id=19, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153558/DR2MLights4_gcectl.jpg'),

        # Listing 20 - Bose Headphones (owner_id 5)
        Listingimage(listing_id=20, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153555/IMG_0964_2_gfhlwk.jpg'),
        Listingimage(listing_id=20, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153553/IMG_0965_1_eff9sh.jpg'),
        Listingimage(listing_id=20, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153554/IMG_0963_uorxi5.jpg'),
        Listingimage(listing_id=20, listing_img=''),

        # Listing 21 - Beats Headphones (owner_id 6)
        Listingimage(listing_id=21, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153535/BoseHeadphones1_gjulhe.jpg'),
        Listingimage(listing_id=21, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153536/BoseHeadphones5_foiz5e.jpg'),
        Listingimage(listing_id=21, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153533/BoseHeadphones3_kchgm3.jpg'),
        Listingimage(listing_id=21, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755153534/BoseHeadphones2_vt4qwd.jpg'),

        # Listing 22 - Vintage Vinyl Record Player (owner_id 6)
        Listingimage(listing_id=22, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755299238/VintageVinylRecorder1_oo709k.jpg'),
        Listingimage(listing_id=22, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755299238/VintageVinylRecorder2_qwe0wb.jpg'),
        Listingimage(listing_id=22, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755299238/VintageVinylRecorder4_afoq9j.jpg'),
        Listingimage(listing_id=22, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755299238/VintageVinylRecorder3_gwmkbp.jpg'),

        # Listing 23 - Wireless Printer (owner_id 6)
        Listingimage(listing_id=23, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755299384/WirelessPrinter3_yi2ckw.jpg'),
        Listingimage(listing_id=23, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755299383/WirelessPrinter1_xa9y4y.jpg'),
        Listingimage(listing_id=23, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755299382/WirelessPrinter2_ppb53y.jpg'),
        Listingimage(listing_id=23, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755299382/WirelessPrinter4_pd8djp.jpg'),

        # Listing 24 - Mountain Bike (owner_id 6)
        Listingimage(listing_id=24, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755299558/MountianBike2_fwy6gg.jpg'),
        Listingimage(listing_id=24, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755299558/MountianBike3_tjheaf.jpg'),
        Listingimage(listing_id=24, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755299559/MountianBike4_izg28d.jpg'),
        Listingimage(listing_id=24, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755299563/MountianBike1_b2nncx.jpg'),

        # Listing 25 - Electric Kettle (owner_id 7)
        Listingimage(listing_id=25, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755300189/ElectricKettle1_uoe8px.jpg'),
        Listingimage(listing_id=25, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755300188/ElectricKettle2_dztx5u.jpg'),
        Listingimage(listing_id=25, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755300188/ElectricKettle4_dvrknm.jpg'),
        Listingimage(listing_id=25, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755300187/ElectricKettle3_uqherd.jpg'),

        # Listing 26 - Leather Office Chair (owner_id 7)
        Listingimage(listing_id=26, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755300582/OfficeChair4_ncpdgm.jpg'),
        Listingimage(listing_id=26, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755300580/OfficeChair3_fzff6e.jpg'),
        Listingimage(listing_id=26, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755300580/OfficeChair2_uokyq8.jpg'),
        Listingimage(listing_id=26, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755300580/OfficeChair1_yrubmu.jpg'),

        # Listing 27 - Air Fryer (owner_id 7)
        Listingimage(listing_id=27, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755300866/AirFryer4_qgm5pv.jpg'),
        Listingimage(listing_id=27, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755300865/AirFryer1_v6gulx.jpg'),
        Listingimage(listing_id=27, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755300863/AirFryer3_cjczt1.png'),
        # Listingimage(listing_id=27, listing_img=''),

        # Listing 28 - Cordless Leaf Blower (owner_id 7)
        Listingimage(listing_id=28, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755308604/LeafBlower3_xc9ext.png'),
        Listingimage(listing_id=28, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755308611/LeafBlower1_yok1x3.jpg'),
        Listingimage(listing_id=28, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755308606/LeafBlower4_ey6pnq.png'),
        Listingimage(listing_id=28, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755308608/LeafBlower2_ujhz5v.png'),

        # Listing 29 - Bluetooth Speaker (owner_id 8)
        Listingimage(listing_id=29, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755301737/Speaker1_bvxnzr.jpg'),
        Listingimage(listing_id=29, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755301736/Speaker4_m6qdgd.jpg'),
        Listingimage(listing_id=29, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755301735/Speaker2_sndptt.jpg'),
        Listingimage(listing_id=29, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755301735/Speaker3_hmc4q4.jpg'),

        # Listing 30 - Cordless Power Drill (owner_id 8)
        Listingimage(listing_id=30, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755310110/DewaltDrill1_k8mb4j.jpg'),
        Listingimage(listing_id=30, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755310121/DewaltDrill2_jkjts8.jpg'),
        Listingimage(listing_id=30, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755310124/DewaltDrill3_a9twtg.jpg'),
        Listingimage(listing_id=30, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755310125/DewaltDrill4_unaoly.jpg'),

        # Listing 31 - Camping Tent (owner_id 8)
        Listingimage(listing_id=31, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755302539/CampTent2_iuhy4q.jpg'),
        Listingimage(listing_id=31, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755302533/CampTent1_dkkntd.jpg'),
        Listingimage(listing_id=31, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755302523/CampTent4_cd7qb0.jpg'),
        Listingimage(listing_id=31, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755302526/CampTent3_w1tz0h.jpg'),

        # Listing 32 - Hand Mixer (owner_id 8)
        Listingimage(listing_id=32, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755302977/HandMixer1_wavcnt.jpg'),
        Listingimage(listing_id=32, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755302979/HandMixer4_ujdd5v.jpg'),
        Listingimage(listing_id=32, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755302980/HandMixer3_vwao23.jpg'),
        Listingimage(listing_id=32, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755302978/HandMixer2_rgcr5z.jpg'),

        # Listing 33 - Gaming Keyboard (owner_id 9)
        Listingimage(listing_id=33, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755303106/GamingKeyboard1_atu0j2.jpg'),
        Listingimage(listing_id=33, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755303107/GamingKeyboard2_oun9x3.jpg'),
        Listingimage(listing_id=33, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755303109/GamingKeyboard4_tesy4i.jpg'),
        Listingimage(listing_id=33, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755303104/GamingKeyboard3_a0tgv7.jpg'),

        # Listing 34 - Snowboard with Bindings (owner_id 9)
        Listingimage(listing_id=34, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755303303/Snowboarding1_vymxbb.jpg'),
        Listingimage(listing_id=34, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755303302/Snowboarding3_lrskt6.jpg'),
        Listingimage(listing_id=34, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755303310/Snowboarding2_thao5p.jpg'),
        Listingimage(listing_id=34, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755303306/Snowboarding4_nccmwo.jpg'),

        # Listing 35 - Smartwatch (owner_id 9)
        Listingimage(listing_id=35, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755303418/Smartwatch1_qbho58.jpg'),
        Listingimage(listing_id=35, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755303418/Smartwatch4_rpzrwu.jpg'),
        Listingimage(listing_id=35, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755303418/Smartwatch2_kzsklg.jpg'),
        Listingimage(listing_id=35, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755303415/Smartwatch3_unuiue.jpg'),

        # Listing 36 - Car Roof Cargo Box (owner_id 9)
        Listingimage(listing_id=36, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755303840/CargoBox2_iuaib5.png'),
        Listingimage(listing_id=36, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755303850/CargoBox4_fhmrax.png'),
        Listingimage(listing_id=36, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755303847/CargoBox1_gysx86.png'),
        Listingimage(listing_id=36, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755303846/CargoBox3_hposyd.png'),

        # Listing 37 - Espresso Machine (owner_id 10)
        Listingimage(listing_id=37, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755303980/ExpressoMachine1_trkfeo.jpg'),
        Listingimage(listing_id=37, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755303977/ExpressoMachine4_mn7ezk.jpg'),
        Listingimage(listing_id=37, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755303985/ExpressoMachine2_ugvghx.jpg'),
        Listingimage(listing_id=37, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755303975/ExpressoMachine3_wlwqc9.jpg'),

        # Listing 38 - Electric Guitar (owner_id 10)
        Listingimage(listing_id=38, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755304111/ElectricGuitar1_qgavj5.jpg'),
        Listingimage(listing_id=38, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755304111/ElectricGuitar1_qgavj5.jpg'),
        Listingimage(listing_id=38, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755304112/ElectricGuitar3_ls8mon.jpg'),
        Listingimage(listing_id=38, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755304108/ElectricGuitar2_hec2et.jpg'),

        # Listing 39 - Cordless Vacuum (owner_id 10)
        Listingimage(listing_id=39, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755304378/Vacuum1_o9xgsu.jpg'),
        Listingimage(listing_id=39, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755304389/Vacuum2_yrhttx.jpg'),
        Listingimage(listing_id=39, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755304395/Vacuum3_lavw8r.jpg'),
        Listingimage(listing_id=39, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755304395/Vacuum4_kgxtpl.jpg'),

        # Listing 40 - Patio Furniture Set (owner_id 10)
        Listingimage(listing_id=40, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755304680/PatioSofa4_vz4rx1.jpg'),
        Listingimage(listing_id=40, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755304684/PatioSofa1_uwz5lf.jpg'),
        Listingimage(listing_id=40, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755304678/PatioSofa3_dimnvp.jpg'),
        Listingimage(listing_id=40, listing_img='https://res.cloudinary.com/dnfeiduuu/image/upload/v1755304676/PatioSofa2_y767qt.jpg'),
    ]

    for image in Listingimages:
        db.session.add(image)
    db.session.commit()

def undo_listingimages():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.Listingimages RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM Listingimages"))

    db.session.commit()
