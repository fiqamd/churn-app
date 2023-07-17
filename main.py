# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 20:05:42 2023

@author: taufiq
"""
# from pycaret.classification import predict_model
import streamlit as st
import pandas as pd
# import numpy as np
import matplotlib
import pickle
import seaborn as sns
import six
import joblib
import sys
import os
import io
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import base64

from matplotlib.backends.backend_pdf import PdfPages
from google.cloud import storage
from st_files_connection import FilesConnection


import warnings
warnings.filterwarnings('ignore')
sys.modules['sklearn.externals.six'] = six

@st.cache(allow_output_mutation=True)
def load_model(bucket_name, model_path):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(model_path)

    # Download the model file to local file
    local_model_path = 'local_model.pkl'
    blob.download_to_file(open(local_model_path, 'wb'))

    # Load the model from local file
    model = joblib.load(local_model_path)

    return model

# # Anda dapat menggunakan fungsi ini untuk meload model Anda
model = load_model("model_churn", "model.pkl")
# @st.cache_resource
# def load_model()
# conn = st.experimental_connection('gcs', type=FilesConnection)
# model_path = conn.read("model_churn/model.pkl", input_format="pkl", ttl=3600)
# # Ganti dengan path file model yang telah Anda simpan
# # model_path = 'model/randfor_new3resampled_mode1.pkl'

# # Muat model
# model = joblib.load(model_path)

area_dict = {'Tangerang': 0, 'Depok': 1, 'Cibubur': 2, 'Bekasi': 3, 'Surabaya': 4, 'Semarang': 5, 'Bogor': 6, 'Malang': 7, 'Palembang': 8, 'Jakarta': 9, 'Medan': 10, 'Bandung': 11, 'Bali': 12, 'Makassar': 13, 'Serang': 14, 'Pekanbaru': 15, 'Lampung': 16, 'Solo': 17, 'Cilegon': 18, 'Karawang': 19, 'Jambi': 20}

plan_dict = {'Value30 Mbps': 0, 'Fast50 Mbps': 1, 'Fast-50 Super93 (1x)': 2, 'Fast50 (PI21-C)': 3, 'Value30 (PI20-B)': 4, 'Nova-100 Super93 (1x)': 5, 'Nova100 (PI20-B)': 6, 'Gamer150 (PI20-B)': 7, 'Fast-50 Super93 (2x)': 8, 'Value30 (PI20-A)': 9, 'Value30 Mbps New': 10, 'Fast50 (PI21-A)': 11, 'Value30 (PI21-B)': 12, 'Fast50 (PI20-B)': 13, 'Nova100 Mbps Lite': 14, 'Value30 Mbps (PA)': 15, 'Nova100 (PI21-B)': 16, 'Fast50 Mbps New': 17, 'Gamer-150 Super93 (2x)': 18, 'Value-30 Super93 (2x)': 19, 'Fast50 (PI21-D)': 20, 'SNAP (Internet Up To 10 Mbps)': 21, 'Value-30 Super93 (1x)': 22, 'BLITZ (Internet Up To 20 Mbps)': 23, 'Fast50 (PI20-A)': 24, 'Hype75 Mbps New': 25, 'Fast50 Special': 26, 'Nova100 Mbps Lite (PA)': 27, 'Nova150 (PI21-B)': 28, 'Value30 (PI21-E)': 29, 'Fast50 Combo': 30, 'Fast.50': 31, 'Gamer 150 Mbps+': 32, 'Gamer50 (PI20-A)': 33, 'Gamer150 Mbps': 34, 'Fast50 (PI21-B)': 35, 'Value30 (PI21-A)': 36, 'Gamer150 (PI21-B)': 37, 'Nova100 (PI20-A)': 38, 'Value30': 39, 'Gamer-150 Super93 (1x)': 40, 'Jet-20 - winback': 41, 'Jet20 (PI20-A)': 42, 'Jet20 Mbps New': 43, 'Nova150 (PI21-A)': 44, 'Nova-100': 45, 'Fast50 (PI21-E)': 46, 'Nova100 (PI21-D)': 47, 'Gamer150 (PI20-A)': 48, 'Hype75 Combo New': 49, 'Fast 50 Mbps+': 50, 'Fast50 Combo New': 51, 'Value-30': 52, 'EazyNet (Bonus TV)': 53, 'Rapid': 54, 'FUN (10 Mbps + TV SD & HD Channels)': 55, 'Jet20 (PI20-B)': 56, 'FUN Promo': 57, 'Nova-100 Super93 (2x)': 58, 'Fast50 Mbps (PA)': 59, 'Nova100 Mbps': 60, 'Jet20 (PI21-A)': 61, 'Value 30 Mbps+': 62, 'Jet20 Internet': 63, 'Nova100+': 64, 'Business 50 (PI20)': 65, 'Gamer150 Mbps Reg': 66, 'SuperNova300 (PI-21)': 67, 'Business 100 (PI20)': 68, 'Magic Wifi 200 (PI21)': 69, 'Gamer150 (PI21-D)': 70, 'Nova 100 Mbps+': 71, 'Value30 Internet': 72, 'Nova100 Combo New': 73, 'SuperNova300+': 74, 'SuperNova-300': 75, 'Value30 Combo': 76, 'Nova100 (PI21-A)': 77, 'Retain 10Mbps': 78, 'Business 300 (PI20)': 79, 'Gamer150 Combo': 80, 'Gamer50': 81, 'Business Pro 150  (PI20)': 82, 'Basic30+': 83, 'MyGamer250 Mbps': 84, 'Business 50 (PI21)': 85, 'Gamer50 (PI21-A)': 86, 'GamerX50': 87, 'Nova100 Special': 88, 'Nova100 Combo (PA)': 89, 'Business 100 Mbps (free installation fee)': 90, 'Business.50 Mbps Reg': 91, 'Gamer-150': 92, 'Business 20 (PI20)': 93, 'Value30 (PI21-D)': 94, 'Fast50 Internet (PA)': 95, 'Business 50 Mbps': 96, 'Basic 30 Mbps': 97, 'Business 30 Mbps (free installation fee)': 98, 'Nova.100+': 99, 'Fast-50': 100, 'Fast50+': 101, 'IBS.CA-Fiber120+ (PI-21)': 102, 'Nova100 Mbps Reg': 103, 'FiberPro 120': 104, 'Business 300 (PI21)': 105, 'Fast50 Internet': 106, 'Nova100 Combo Internet A': 107, 'Business 100 (PI21)': 108, 'Business Pro 150 (PI21)': 109, 'Business 100 Mbps (Promo Buy 1 Get 1)': 110, 'IBS.CA-Fiber60+ (PI-21)': 111, 'Value30 (PI21-C)': 112, 'Nova150 Special 2': 113, 'Business 20 Mbps': 114, 'FiberPro 60 (PI-21)': 115, 'Value30 Special 2': 116, 'Basic8': 117, 'IBS.CA Business30 (PI-21)': 118, 'IBS.CA-Fiber60+': 119, 'Business 20 (PI21)': 120, 'Gamer150 Mbps New': 121, 'Nova100 (PI21-C)': 122, 'Business Pro 500 (PI20)': 123, 'Basic15+': 124, 'Hype75 Internet': 125, 'Business 100 Mbps': 126, 'Nova150 Special': 127, 'IBS.CA Roket100 (PI-21)': 128, 'Business 30 Mbps': 129, 'Nova 100 Mbps+ XTRA': 130, 'Fast50 Special 2': 131, 'IBS.CA Business30': 132, 'Gamer150 Mbps Reg (PA)': 133, 'Value30 Combo New': 134, 'Business 300 Mbps': 135, 'FiberPro 20': 136, 'Fast50 Combo (PA)': 137, 'Gamer150 Combo (PA)': 138, 'Business.300 Mbps Reg': 139, 'Tanpa Plan': 140, 'Value30 Special': 141, 'Jet-20': 142, 'Jet20 Combo New': 143, 'Jet20 Mbps': 144, 'Gamer150 (PI21-A)': 145, 'Jet20 Combo': 146, 'Jet20': 147, 'Nova100 Mbps New': 148, 'Jet20 (PI21-D)': 149, 'Business Pro 150 Mbps': 150, 'Gamer-150 (fs)': 151, 'Business Pro 500 Mbps': 152, 'Alpha 10 Mbps': 153, 'GAMER150+': 154, 'Business50 Mbps (PA)': 155, 'Nova100 Combo': 156, 'Jet20 Lite': 157, 'FiberPro 120 (PI-21)': 158, 'IBS.CA Business 50 Mbps (PI-21)': 159, 'Value30 Combo (PA)': 160, 'Fast50 Mbps+ Xtra ComboTV': 161, 'FiberPro 20 (PI-21)': 162, 'Gamer-150 (smt)': 163, 'Jet20 (PI21-C)': 164, 'Fast-50 (fs)': 165, 'Fast50 Combo Internet A': 166, 'Value-30 (bit)': 167, 'Fast-50 (smt)': 168, 'Business Pro 500 (PI21)': 169, 'Value-30 (fs)': 170, 'Nova-100 (fs)': 171, 'Value-30 (smt)': 172, 'Hype75 Combo Internet A': 173, 'FiberPro 60': 174, 'Jet 20 PLUS': 175, 'Value30 Mbps+ Xtra ComboTV': 176, 'Jet20 (PI21-B)': 177, 'Jet 20 PLUS AP12': 178, 'Nova-100 (smt)': 179, 'Gamer 150 Mbps+ Xtra ComboTV': 180, 'Nova-100 (bit)': 181, 'Jet 20 PLUS AP6': 182, 'Gamer150 (PI21-C)': 183, 'BusinessPro.150 Mbps Reg': 184, 'Magic Wifi 200': 185, 'Jet 20 Mbps+': 186, 'Value30 Combo Internet A': 187, 'Nova100 Internet': 188, 'Gamer 75 Mbps+': 189, 'Nova100 Mbps Reg (PA)': 190, 'Jet 20 Mbps+ HITS': 191, 'Fast 50 Mbps+ XTRA': 192, 'Value 30 Mbps+ XTRA': 193, 'Gamer 150 Mbps+ XTRA': 194, 'Value 30 Mbps+ HITS': 195, 'Gamer150 Mbps New (PA)': 196, 'Gamer150 Combo New': 197, 'Fast-50 (bit)': 198, 'Jet20 Mbps+ Xtra ComboTV': 199, 'Nova 100 Mbps+ Xtra ComboTV': 200, 'Gamer 75 Mbps+ XTRA': 201, 'Gamer 75 Mbps+ Xtra ComboTV': 202, 'SuperNova-300 (fs)': 203, 'IBS.CA Business 50 Mbps': 204, 'IBS.CA Business Pro 150 Mbps': 205, 'Nova 100 Mbps+ HITS': 206, 'Fast 50 Mbps+ HITS': 207, 'Value30 New (PA)': 208, 'Sonic150 Combo': 209, 'Flash75 ComboTV Pakubuwono': 210, 'Gamer150 ComboTV Pakubuwono': 211, 'Supernova300 ComboTV Pakubuwono': 212, 'IBS.CA Business20': 213, 'Fast50 Via Alma': 214, 'Gamer200 Mbps Pakubuwono': 215, 'IBS.CA Business300': 216, 'Jet20 Mbps (PA)': 217, 'Business20 Mbps (PA)': 218, 'Jet20 Combo (PA)': 219, 'Business100 Mbps (PA)': 220, 'FiberPro 300': 221, 'Business300 Mbps (PA)': 222, 'BusinessPro 150 Mbps (PA)': 223, 'Value30 Internet (PA)': 224, 'VIP NRO 2021': 225, 'Nova100 Mbps Pakubuwono': 226, 'VIP NRO 2021 (FS)': 227, 'BusinessPro 500 Mbps (PA)': 228, 'VIP NRO 2021+': 229, 'IBS.CA Business100': 230, 'Value30 Combo New (PA)': 231, 'Nova100 Mbps New (PA)': 232, 'Hype75 Mbps New (PA)': 233, 'Fast50 Mbps New (PA)': 234, 'Jet20 Combo Internet A': 235, 'Fast50 Combo New (PA)': 236, 'Gamer150 Combo New (PA)': 237, 'Fast50 Internet (AP77)': 238, 'Value30 Internet (AP77)': 239, 'MyGamer250 Internet (AP77)': 240, 'Nova 100 Internet (AP77)': 241, 'Value30 Combo Internet A (AP77)': 242, 'MyGamer250 Combo Internet A': 243, 'Hype75 Combo Internet A (PA)': 244, 'Nova 100 Internet (PA)': 245, 'Value30 Combo Internet A (PA)': 246, 'Fast50 Combo Internet A (PA 12 Get 6)': 247, 'MyGamer250 Combo Internet A (PA 12 Get 6)': 248, 'MyGamer250 Mbps Internet (PA)': 249, 'Value30 (PI-22F)': 250, 'Nova100 (PI-22I)': 251, 'Fast50 (PI-22H)': 252, 'Nova100 (PI-22B)': 253, 'Gamer150 (PI-22C)': 254, 'Fast50 (PI-22I)': 255, 'BSD Value (100 Mbps + TV)': 256, 'Value30 (PI-22M)': 257, 'Nova100 Combo Internet A (PA)': 258, 'BSD Smash (300 Mbps + TV)': 259, 'MyGamer250 Combo Internet A (PA)': 260, 'Gamer150 (PI-22D)': 261, 'VALUE PROMO': 262, 'Value30 (PI-22H)': 263, 'VALUE SUPER (Internet Up To 1 Mbps + TV Channel)': 264, 'Nova100 (PI-22E)': 265, 'Fast50 (PI-22G)': 266, 'Snap Plus (Bonus TV)': 267, 'Package Internet Up To 10 Mbps & TV Starter 15+': 268, 'Value30 (PI-22G)': 269, 'Fast50 Combo Internet A (PA)': 270, 'BSD Basic 10 Mbps': 271, 'Fast50 (PI-22C)': 272, 'Basic Plus Star': 273, 'Value30 (PI-22I)': 274, 'Nova Plus Cosmic': 275, 'Basic Plus Cosmic': 276, 'Value30 (PI-22K)': 277, 'BASIC SUPER (Internet Up To 512 Kbps + TV Channel)': 278, 'Nova100 (PI-22J)': 279, 'AMAZING (50 Mbps + TV SD & HD Channels)': 280, 'BSD Pro 300 Mbps': 281, 'Nova100 (PI-22H)': 282, 'Bright': 283, 'Gamer50 (PI-22C)': 284, 'Value30 (PI-22J)': 285, 'Value30 (PI-22N)': 286, 'Hype75 (PI-22A)': 287, 'Gamer150 (PI-22A)': 288, 'Gamer150 (PI-22B)': 289, 'Nova100 (PI-22L)': 290, 'Nova150 (PI-22A)': 291, 'Fast50 (PI-22B)': 292, 'Nova150 (PI-22B)': 293, 'Nova100 (PI-22D)': 294, 'Lite (Package Internet Up To 3 Mbps & TV)': 295, 'FESTIVE (40 Mbps + TV SD & HD Channels)': 296, 'Internet Up To 512 Kbps': 297, 'Internet Up To 3 Mbps': 298, 'SuperNova Package': 299, 'Value30 (PI-22C)': 300, 'Gamer150+ XTRA (PI-22A)': 301, 'Nova100 (PI-22C)': 302, 'Fast50 (PI-22A)': 303, 'Value30 Combo (PI-22B)': 304, 'SUPER (20 Mbps + TV SD & HD Channels) KOWIS LEWIS': 305, 'Jet20 (PI-22G)': 306, 'XTREME (100 Mbps + TV SD & HD Channels)': 307, 'Supernova300 Mbps (PA)': 308, 'Value30 (PI-22D)': 309, 'Fast50 Combo (PI-22A)': 310, 'Jet20 (PI-22E)': 311, 'Jet20 (PI-22A)': 312, 'Fast50 Combo (PI-22C)': 313, 'Nova100 (PI-22M)': 314, 'Nova100 Combo (PI-22B)': 315, 'Jet20 (PI-22K)': 316, 'SUPER Promo': 317, 'Fast50 (PI-22E)': 318, 'Jet20 (PI-22C)': 319, 'Fast50 (PI-22D)': 320, 'Fast50 Combo (PI-22B)': 321, 'Nova100 (PI-22G)': 322, 'Business100 (PI-22B)': 323, 'Business20 (PI-22B)': 324, 'Fast50 (PI-22K)': 325, 'Business300 (PI-22C)': 326, 'Fast50 (PI-22F)': 327, 'Basic15': 328, 'Business50 (PI-22C)': 329, 'Jet20 (PI-22D)': 330, 'Value30 (PI-22A)': 331, 'Nova100 Combo (PI-22A)': 332, 'Basic (promo tv booster)': 333, 'Gamer (promo tv booster)': 334, 'Value30 (PI-22E)': 335, 'Starter 6 Mbps': 336, 'Fast50 (PI-22J)': 337, 'BusinessPro150 (PI-22D)': 338, 'Business50 (PI-22B)': 339, 'Business100 (PI-22A)': 340, 'Business300 (PI-22B)': 341, 'Nova100 (PI-22F)': 342, 'Gamer50 (PI-22A)': 343, 'Business20 (PI-22A)': 344, 'GamerX.50+': 345, 'Nova (promo tv booster)': 346, 'Fast50 (PI-22L)': 347, 'MyGamer250 Combo Internet A (PA 12 Get 12)': 348, 'Nova Package': 349, 'Business 10 Mbps (free installation fee)': 350, 'Value30 Combo (PI-22A)': 351, 'Nova Plus Star': 352, 'Business50 (PI-22A)': 353, 'Nova Plus Star (diskon 25% 12 bulan)': 354, 'Business 10 Mbps': 355, 'GAMERX50+': 356, 'Nova100 (PI-22A)': 357, 'BusinessPro150 (PI-22C)': 358, 'Business300 (PI-22A)': 359, 'BusinessPro150 (PI-22B)': 360, 'IBS.CA Roket100': 361, 'IBS.CA-Fiber120+': 362, 'Business 300 Mbps (Promo Buy 1 Get 1)': 363, 'Basic.15+': 364, 'GAMER.150+': 365, 'IBS.CA Business300 (PI-21)': 366, 'Business 300 Mbps (free installation fee)': 367, 'Retain 10Mbps AdvanceTV': 368, 'Basic.8+': 369, 'IBS.CA Business100 (PI-21)': 370, 'Jet20 Combo (PI-22A)': 371, 'Business Pro 100 Mbps': 372, 'FiberPro 300 (PI-21)': 373, 'MyGamer250 Internet (PA 12 Get 12)': 374, 'Value30 (PI-22B)': 375, 'Nova100 Combo New (PA)': 376, 'Value30 Internet (PA 12 Get 12)': 377, 'Fast 50 Mbps': 378, 'Hype75 Combo New (PA)': 379, 'Gamer50 (PI-22B)': 380, 'Business 75 (PI20)': 381, 'Jet20 Internet (PA)': 382, 'Jet20 (PI-22B)': 383, 'Business Pro 500Mbps Bridge Mode ONT': 384, 'BusinessPro150 (PI-22A)': 385, 'Jet20 (PI-22I)': 386, 'Jet20 (PI-22H)': 387, 'Jet20 (PI-22F)': 388, 'Hype75 Internet (PA)': 389, 'Gamer-150 (bit)': 390, 'Business 100 (WEJ)': 391, 'Nova100 Via Alma': 392, 'Business 100Mbps Via Alma': 393, 'Sonic150 Combo (PA)': 394, 'Nova100 Mbps Pakubuwono Menteng': 395, 'Fast50 Internet (PA 12 Get 12)': 396, 'Fantastic300 Mbps New': 397, 'Demoline PoP 50 Mbps': 398, 'Gamer150 Via Alma': 399, 'Internet 750Mbps New': 400, 'Pride 1 Gbps New': 401, 'Prime500 Mbps New': 402, 'Nova150 Mbps Pakubuwono Menteng': 403, 'Hype75 Internet (AP77)': 404, 'Fast50 Combo Internet A (AP77)': 405, 'MyGamer250 Combo Internet A (AP77)': 406, 'Nova100 Combo Internet A (AP77)': 407, 'Hype75 Combo Internet A (AP77)': 408, 'Supernova400 Mbps Pakubuwono': 409, 'Ultra 1 Gbps Combo Internet A': 410, 'Internet VIP NRO': 411, 'Ultra 1Gbps Internet': 412, 'VIP Rumah Ibadah': 413, 'Fast50 Internet (PA 12 Get 6)': 414, 'MyGamer250 Internet (PA 12 Get 6)': 415, 'Nova 100 Internet (PA 12 Get 6)': 416, 'Nova150 Combo Anandamaya New': 417, 'Nova100 Combo Anandamaya': 418, 'Fast50 Combo Anandamaya': 419, 'Value30 Combo Internet A (PA 12 Get 12)': 420, 'Jet20 Internet (PA3)': 421, 'Nova100 Combo Internet A (PA 12 Get 12)': 422, 'Fast50 Combo Internet A (PA 12 Get 12)': 423, 'Jet20 Combo Internet A (PA3)': 424, 'Jet20 Internet (PA6)': 425, 'Nova100 Internet (PA 12 Get 12)': 426, 'Value30 Internet (PA3)': 427, 'Value30 Internet (PA6)': 428, 'MyGamer250 Combo Internet A (PA3)': 429, 'Value30 Combo Internet A (PA6)': 430, 'Nova 100 Internet (PA3)': 431, 'Jet20 Combo Internet A (PA6)': 432, 'Fast50 Internet (PA3)': 433, 'MyGamer250 Internet (PA3)': 434, 'Fast50 Internet (PA6)': 435, 'Value30 Internet (PA 12 Get 6)': 436, 'Value30 Combo Internet A (PA3)': 437, 'Fast50 Combo Internet A (PA6)': 438, 'Fast50 Combo Anandamaya NEW': 439, 'Nova 100 Internet (PA6)': 440, 'MyGamer250 Internet (PA6)': 441}

dict_tvplan = {'Tanpa Plan': 0, 'StarTV': 1, 'SmarTV+': 2, 'Local Channel': 3, 'STAR': 4, 'Basic TV': 5, 'Cosmic TV': 6, 'Combo TV (Fast50)': 7, 'SmarTV': 8, 'No Channel': 9, 'Combo TV (Hype75)': 10, 'SMARTV': 11, 'Combo TV (Nova100)': 12, 'Combo TV (Value30)': 13, 'Combo TV (Gamer150)': 14, 'TV SOHO B (Movies and Sports)': 15, 'Nova100 Mbps (ComboTV+ELKMS)': 16, 'SMARTV+': 17, 'Cosmic TV SOHO': 18, 'Advance TV': 19, 'TV SOHO A (News and lifestyle)': 20, 'Star TV SOHO': 21, 'Star TV Plus': 22, 'StarTV Jet': 23, 'Jet20 Mbps (ComboTV)': 24, 'Combo TV (Jet20)': 25, 'BASIC': 26, 'Fast50 Mbps (ComboTV+ELKMS)': 27, 'Xtra ComboTV (Fast50)': 28, 'Hype75 Mbps (ComboTV+ELKMS)': 29, 'Xtra ComboTV (Value30)': 30, 'Xtra ComboTV (Gamer150)': 31, 'Value30 Mbps (ComboTV+ELK)': 32, 'Star TV Plus (Android)': 33, 'Xtra ComboTV (Jet20)': 34, 'Xtra ComboTV (Nova100)': 35, 'Xtra ComboTV (Gamer75)': 36, 'Xtra ComboTV (Fast50 + ELKMS)': 37, 'Xtra ComboTV (V30 + ELK)': 38, 'Xtra ComboTV Jet20 (Android)': 39, 'Combo TV (Sonic150)': 40, 'ComboTV Pakubuwono': 41, 'ComboTV 77 Channel': 42, 'Star TV': 43, 'No Channel (0)': 44, 'TV Only 60 Channel': 45, 'TV Starter 15+': 46, 'Local Channel (Android)': 47, 'Advance TV (Android)': 48, 'SOHO A': 49, 'ComboTV Pakubuwono (Android)': 50}

dict_promo = {'Tanpa Advance Promo': 0, 'Kompensasi Diskon (Disc.50% x 3)': 1, 'Promo Upsell 15% (Fast50 Mbps New) 6 bulan': 2, 'RWB Promo Diskon 25% X 3': 3, 'RWB Promo Diskon 50% X 6': 4, 'Kompensasi Diskon (Disc.25% x 3)': 5, 'RWB Promo Diskon 35%': 6, 'Discount 30000 - PI21 (11Months)': 7, 'Discount 15000 - PI21 (11months)': 8, 'RWB Promo Diskon 35% X 6': 9, 'Upsell Discount (20% 3 Months)': 10, 'Promo Upsell 15% (Hype75 Mbps Combo New) 6 bulan': 11, 'Promo Sinarmas Employee': 12, 'Kompensasi Diskon (Disc.15% x 3)': 13, 'Promo Upsell 15% (Fast50 Mbps Combo New) 6 bulan': 14, 'Kompensasi Diskon (Disc.25% x 2)': 15, 'Kompensasi Diskon (Disc.20% x 3)': 16, 'Promo Upsell  Disc 15% (6 Bulan) Fast50': 17, 'Promo Disc 20% (12 Bulan) Jet20 Mbps Combo New': 18, 'RWB Promo Diskon 10% x 3 ': 19, 'Promo Upsell 15% (Gamer150 New) 6 Bulan': 20, 'Discount 10000 - PI21 (12Months)': 21, 'Discount 30000 - PI21 (12Months)': 22, 'Advance Payment Promo 9+3 (Existing)': 23, 'Kompensasi Diskon (Disc.10% x 3)': 24, 'RWB Promo Diskon 25% X 6': 25, 'Discount 40000 - PI21 (11Months)': 26, 'Promo Upsell 15% (Value30 Mbps Combo New) 6 bulan': 27, 'RWB Promo Diskon 50% X 3': 28, 'Promo Upsell Disc 15% (6 Bulan) Fast50 Combo A': 29, 'Promo Upsell 15% (Hype75 Mbps New) 6 bulan': 30, 'Promo Upsell Disc 15% (6 Bulan) Hype75 Combo A': 31, 'Promo Upsell (Disc 15% 6 Bulan) MyGamer250 Mbps': 32, 'Credit Card Payment Reward Discount (For Xtra)': 33, 'Promo Upsell 15% (Value30 Mbps New) 6 bulan': 34, 'Promo Upsell  Disc 15% (6 Bulan) Hype75': 35, 'Credit Card Payment Reward Discount': 36, 'Promo Upsell Disc 15% (6 Bulan) Value30 Combo A': 37, 'Discount 15000 - PI21 (12months)': 38, 'Advance Payment Promo 9+3 (New SA)': 39, 'Promo Upsell  Disc 15% (6 Bulan) Nova100': 40, 'New Year 2020 Promo (Bus 100 - 300)': 41, 'New Year 2020 Promo (Bus 50)': 42, 'New Year 2020 Promo (Bus Pro 150 - Pro 500)': 43, 'Promo Ramadhan Up to 30% 2021 (Nova100 Mbps, Nova100 Combo, Sonic150 Combo)': 44, 'Advance Payment Promo 9+3 (After SA)': 45, 'Promo Ramadhan Up to 30% 2021 (Fast50 Mbps)': 46, 'Promo Ramadhan Up to 30% 2021 (Fast50 Combo, Gamer150 Mbps, Gamer150 Combo)': 47, 'Jet20 Mbps Special Discount 20%': 48, 'Jet20 Mbps Special Discount 20% (6 Months)': 49, 'Promo Dismantle 25% (Fast50 Mbps, Fast50 Combo, Business 50)': 50, 'Promo Diskon Khusus Apartment Via Alma (100%)': 51, 'Jet20 Mbps Special Discount 20% - Promo September 2021 (6 Months)': 52, 'Nova100 Mbps Reg Discount 30% (for 6 Months)': 53, 'Kompensasi Diskon (Disc.10% x 2)': 54, '12 Month Advance Payment (Existing Customer)': 55, 'Promo Sumpah Pemuda - 2021 (All Res)': 56, 'Promo Hari Pahlawan - 2021 (All Res)': 57, 'Promo Hari Pahlawan - 2021 (Sonic)': 58, 'Promo Hari Pahlawan - 2021 (Gamer Combo)': 59, 'Promo Akhir Tahun - 2021 (All Res)': 60, 'Promo Akhir Tahun - 2021 (Gamer150 Mbps Reg)': 61, 'Promo Akhir Tahun - 2021 (Nova100 Combo)': 62, 'Promo Akhir Tahun - 2021 (All Business)': 63, 'Promo New Area (Value30 Mbps New) 12 bulan': 64, 'Promo Tahun Baru Disc 25% (6 Bulan)  Nova 100 Mbps Combo New': 65, 'Promo Akhir Tahun - 2021 (Gamer Combo)': 66, 'Promo New Area (Value30 Mbps Combo New) 12 bulan': 67, 'Promo New Area (Hype75 Mbps New) 12 bulan': 68, 'Promo Tahun Baru Disc 25% (6 Bulan) Nova 100 Mbps New ': 69, 'Promo New Area (Fast50 Mbps New) 12 bulan': 70, 'Promo New Area (Fast50 Mbps Combo New) 12 bulan': 71, 'Promo New Area (Fast50 Mbps New) 6 bulan': 72, 'Promo Tahun Baru Disc 25% (6 Bulan)  Gamer 150 Mbps New ': 73, 'Promo New Area (Fast50 Mbps Combo New) 6 bulan': 74, 'Promo Tahun Baru Disc 25% (6 Bulan)  Gamer 150 Mbps New': 75, 'Promo New Area (Gamer150 New) 6 Bulan': 76, 'Promo Tahun Baru Disc 25% (6 Bulan) Nova 100 Mbps New': 77, 'Promo New Area (Value30 Mbps New) 6 bulan': 78, ' Promo Special Thamrin Residence Disc 20% (6 Bulan) Fast50 Mbps New ': 79, 'Promo New Area (Hype75 Mbps New) 6 bulan': 80, 'Promo New Area (Value30 Mbps Combo New) 6 bulan': 81, 'Promo Imlek Disc 15% (6 Bulan) Hype 75 Mbps New': 82, 'Promo Imlek Disc 25% (6 Bulan)  Gamer 150 Mbps New': 83, 'Promo Imlek Disc 25% (6 Bulan) Nova 100 Mbps New ': 84, 'Promo New Area (Nova100 New) 6 Bulan': 85, 'Promo Special Thamrin Residence Disc 20% (6 Bulan) Hype75 Mbps New': 86, 'Promo Special Thamrin Residence Disc 20% (6 Bulan) Gamer150 Combo New': 87, 'Promo New Area Disc 20% (12 Bulan) Jet20 Mbps New': 88, 'Promo Disc 20% (12 Bulan) Value30 Mbps New': 89, 'Promo New Area Disc 20% (12 Bulan) Value30 Mbps New': 90, 'Promo New Area Disc 20% (12 Bulan) Value30 Mbps Combo New': 91, 'Promo New Area Disc 20% (12 Bulan) Fast50 Mbps New': 92, 'Promo New Area Disc 20% (12 Bulan) Jet20 Mbps Combo New': 93, 'Promo Disc 20% (12 Bulan) Fast50 Mbps Combo New': 94, 'Promo New Area Disc 20% (12 Bulan) Nova100 Mbps Combo New': 95, 'Promo New Area Disc 20% (12 Bulan) Hype75 Mbps New': 96, 'Promo Disc 20% (12 Bulan) Jet20 Mbps New': 97, 'Promo Imlek Disc 25% (6 Bulan)  Nova 100 Mbps Combo New ': 98, 'Promo Disc 20% (12 Bulan) Fast50 Mbps New': 99, 'Promo Disc 20% (12 Bulan) Value30 Mbps Combo New': 100, 'Promo Disc 20% (12 Bulan) Business20 Mbps': 101, 'Promo Disc 20% (12 Bulan) Gamer150 Mbps New': 102, 'Promo Disc 20% (12 Bulan) Hype75 Mbps New': 103, 'Promo Special Thamrin Residence Disc 20% (6 Bulan) Nova100 Mbps New ': 104, 'Promo Nasional 2022 Disc 15% (6 Bulan) Nova100 Mbps New': 105, 'Promo Disc 20% (12 Bulan) Nova100 Mbps New': 106, 'Promo Nasional 2022 Disc 15% (6 Bulan) Nova100 Mbps Combo New': 107, 'Promo Disc 20% (12 Bulan) Hype75 Mbps Combo New': 108, 'Promo Thamrin Residence Disc 20% (6 Bulan) Fast50': 109, 'Promo Nasional 2022 Disc 15% (6 Bulan) Gamer150 Mbps New': 110, 'Promo Disc 20% (12 Bulan) Nova100 Mbps Combo New': 111, 'Promo Nasional 2022 Disc 15% (6 Bulan) Gamer150 Mbps Combo New': 112, 'Promo Ramadhan - Idul Fitri Disc 20% (12 Bulan) Fast50 Mbps Combo New': 113, 'Promo Ramadhan - Idul Fitri Disc 20% (12 Bulan) Fast50 Mbps New': 114, 'Promo Ramadhan - Idul Fitri Disc 20% (12 Bulan) Gamer150 Mbps New': 115, 'Promo Ramadhan - Idul Fitri Disc 20% (12 Bulan) Hype75 Mbps New': 116, 'Promo Disc 20% (12 Bulan) Business50 Mbps': 117, 'Promo Ramadhan - Idul Fitri Disc 20% (12 Bulan) Gamer150 Mbps Combo New': 118, 'Promo Ramadhan - Idul Fitri Disc 20% (12 Bulan) Nova100 Mbps New': 119, 'Promo Ramadhan - Idul Fitri Disc 20% (12 Bulan) Nova100 Mbps Combo New': 120, 'Promo Ramadhan - Idul Fitri Disc 20% (12 Bulan) Hype75 Mbps Combo New': 121, 'Promo Ultah MyRep Disc 20% + 7% (12 Bulan) Fast50 Mbps New': 122, 'Promo Ultah MyRep Disc 20% + 7% (12 Bulan) Hype75 Mbps New': 123, 'Promo Ultah MyRep Disc 20% + 7% (12 Bulan) Gamer150 Mbps Combo New': 124, 'Promo Ultah MyRep Disc 20% + 7% (12 Bulan) Gamer150 Mbps New': 125, 'Promo Ultah MyRep Disc 20% + 7% (12 Bulan) Fast50 Mbps Combo New': 126, 'Promo Ultah MyRep Disc 20% + 7% (12 Bulan) Nova100 Mbps New': 127, 'Promo Ultah MyRep Disc 20% + 7% (12 Bulan) Hype75 Mbps Combo New': 128, 'Promo Special Fast50 Mbps Disc 25% 12 Bulan': 129, 'Promo Disc 20% (12 Bulan) Business100 Mbps': 130, 'Promo Special Fast50 Combo Disc 25% 12 Bulan': 131, 'Promo New Area (Gamer150 Combo New) 12 Bulan': 132, 'Promo Disc 20% (12 Bulan) Business300 Mbps': 133, 'Promo Disc 20% (12 Bulan) Value30 Combo A': 134, 'Promo Disc 20% (12 Bulan) Jet20 Combo A': 135, 'Promo Switching 2022 Disc 30% (12 Bulan) Jet20 Mbps Combo New': 136, 'Promo Switching 2022 Disc 30% (12 Bulan) Jet20 Mbps New': 137, 'Promo Switching 2022 Disc 30% (12 Bulan) Fast50 Mbps New': 138, 'Promo Switching 2022 Disc 30% (12 Bulan) Hype75 Mbps New': 139, 'Promo Switching 2022 Disc 30% (12 Bulan) Value30 Mbps New': 140, 'Promo Switching 2022 Disc 30% (12 Bulan) Fast50 Mbps Combo New': 141, 'Promo Switching 2022 Disc 30% (12 Bulan) Hype75 Mbps Combo New': 142, 'Promo Switching 2022 Disc 30% (12 Bulan) Value30 Mbps Combo New': 143, 'Promo Switching 2022 Disc 30% (12 Bulan) Nova100 Mbps Combo New': 144, 'Promo Switching 2022 Disc 30% (12 Bulan) Gamer150 Mbps New': 145, 'Promo New RFS Pekanbaru Disc 15% Jet20 Mbps New': 146, 'Promo Disc 20% (12 Bulan) Business50 Mbps + TV': 147, 'Promo Disc 20% (12 Bulan) Gamer150 Mbps Combo New': 148, 'Promo New RFS Disc 15% Jet20 Mbps New': 149, 'Promo Disc 20% (12 Bulan) Jet20': 150, 'Promo New RFS Disc 15% Value30 Mbps New': 151, 'Promo CLBK Disc 25% (12 Bulan) Value30 Mbps New': 152, 'Promo CLBK Disc 25% (12 Bulan) Jet20 Mbps New': 153, 'Promo New RFS Disc 25% Fast50 Mbps New': 154, 'Promo New RFS Disc 25% Hype75 Mbps New': 155, 'Promo New RFS Disc 15% Jet20 Mbps Combo New': 156, 'Promo Disc 20% (12 Bulan) Fast50': 157, 'Promo Disc 20% (12 Bulan) Value30': 158, 'Promo New RFS Disc 25% Nova100 Mbps New': 159, 'Promo Disc 20% (12 Bulan) Hype75': 160, 'Promo CLBK Disc 25% (12 Bulan) Nova100 Mbps New': 161, 'Promo Disc 15% (12 Bulan) Jet20': 162, 'Promo Merdeka Disc 25% 6 Bulan (MyGamer250)': 163, 'Promo Disc 20% (12 Bulan) Nova100': 164, 'Promo Disc 20% 12 Bulan MyGamer250 Mbps': 165, 'Promo Merdeka Disc 25% 6 Bulan (Nova100)': 166, 'Promo Merdeka Disc 25% 6 Bulan (Nova100 Combo A)': 167, 'Promo Disc 15% (12 Bulan) Value30': 168, 'Promo CLBK Disc 25% (12 Bulan) Fast50 Internet': 169, 'Promo CLBK Disc 25% (12 Bulan) Jet20 Combo A': 170, 'Promo Disc 15% (12 Bulan) Jet20 Combo A': 171, 'Promo Disc 20% (12 Bulan) Hype75 Combo A': 172, 'Promo CLBK Disc 25% (12 Bulan) Jet20 Internet\t': 173, 'Promo Disc 20% (12 Bulan) Nova100  Combo A': 174, 'Promo Disc 20% (12 Bulan) Fast50 Combo A': 175, 'Promo Nasional Disc 15% 6 Bulan (Nova100)': 176, 'Promo Harbolnas September Value30 Internet': 177, 'Promo Harbolnas September Fast50 Internet': 178, 'Promo Harbolnas September Value30 Combo A': 179, 'Promo Nasional (Disc 15% 6 Bulan) MyGamer250 Mbps': 180, 'Promo Harbolnas September Nova100 Internet': 181, 'Promo Harbolnas September Fast50 Combo A': 182, 'Promo Harbolnas September MyGamer250 Internet': 183, 'Promo Nasional Disc 15% 6 Bulan (Nova100 Combo A)': 184, 'Promo Disc 15% (12 Bulan) Fast50': 185, 'Promo New RFS HRB Disc 20% (6 Bulan) Fast50': 186, 'Promo Disc 25% (12 Bulan) Fast50 Combo A': 187, 'Promo Oktober 2022 Disc 25% (12 Bulan) Fast50 Internet': 188, 'Promo Oktober 2022 Disc 25% (12 Bulan) Nova100 Internet': 189, 'Promo Shocktober Disc 25% (12 Bulan) Jet20': 190, 'Promo Shocktober Disc 30% (12 Bulan) Nova100 Combo A': 191, 'Promo Shocktober Disc 25% (12 Bulan) Value30 Combo A': 192, 'Promo Shocktober Disc 25% (12 Bulan) Value30 Internet': 193, 'Promo Shocktober Disc 30% (12 Bulan) Fast50 Internet': 194, 'Promo Disc 20% (12 Bulan) BusinessPro500 Mbps': 195, 'Promo WOW FLASH SALE Value30 Internet': 196, 'Promo WOW FLASH SALE Value30 Combo A': 197, 'Promo WOW-VEMBER DEALS Value30 Internet': 198, 'Promo WOW-VEMBER DEALS Fast50 Combo A': 199, 'Promo WOW-VEMBER DEALS Fast50 Internet': 200, 'Promo WOW-VEMBER DEALS Value30 Combo A': 201, 'Promo MyRep YES Value30 Internet': 202, 'Kompensasi Diskon (Disc.50% x 2)': 203, 'Kompensasi Diskon (Disc.15% x 2)': 204, 'Promo Upsell (Disc 15% 6 Bulan) MyGamer250 Combo A': 205, 'Promo Upsell 15% (Gamer150 Combo New) 6 Bulan': 206, 'Promo Upsell Disc 15% (6 Bulan) Nova100 Combo A': 207, 'Promo Upsell 15% (Nova100 New) 6 Bulan': 208, 'Promo New Area (Nova100 Combo New) 12 Bulan': 209, 'Promo Upsell  Disc 15% (6 Bulan) Value30': 210, '3 Month Advance Payment': 211, 'Discount 40000 - PI21 (12Months)': 212, 'Discount 35000 - PI21 (12Months)': 213, 'Kompensasi Diskon (Disc.50% x 1)': 214, 'Kompensasi Diskon (Disc.10% x 1)': 215, 'Kompensasi Diskon (Disc.15% x 1)': 216, 'Kompensasi Diskon (Disc.20% x 1)': 217, 'Kompensasi Diskon (Disc.25% x 1)': 218, 'Discount VIP NRO 2021 (12months)': 219, 'Promo New Area (Nova100 New) 12 Bulan': 220, '12 Month Advance Payment (New SA)': 221, 'Advance Payment 6 Month': 222, 'Promo Tahun Baru Disc 25% (6 Bulan)  Gamer 150 Mbps Combo New': 223, 'Promo New Area Disc 20% (12 Bulan) Gamer150 Mbps New': 224, 'Promo New Area Disc 20% (12 Bulan) Nova100 Mbps New': 225, 'Promo New Area Disc 20% (12 Bulan) Gamer150 Mbps Combo New': 226, 'Promo New Area Disc 20% (12 Bulan) Fast50 Mbps Combo New': 227, 'Promo New Area Disc 20% (12 Bulan) Business20 Mbps + TV': 228, 'Promo New Area Disc 20% (12 Bulan) Business20 Mbps': 229, 'Promo Disc 20% (12 Bulan) Business20 Mbps + TV': 230, 'Discount VIP NRO 2021 (24months)': 231, 'Promo Ultah MyRep Disc 20% + 7% (12 Bulan) Nova100 Mbps Combo New': 232, 'Promo Disc 20% (12 Bulan) BusinessPro150 Mbps': 233, 'Discount VIP NRO 2021 (36months)': 234, 'Disc Demoline PoP 50 Mbps': 235, 'Promo Switching 2022 Disc 30% (12 Bulan) Nova100 Mbps New': 236, 'Promo Switching 2022 Disc 30% (12 Bulan) Gamer150 Mbps Combo New': 237, 'Promo New RFS Pekanbaru Disc 15% Jet20 Mbps Combo New': 238, 'Promo CLBK Disc 25% (12 Bulan) Value30 Mbps Combo New': 239, '3 Months Advance Payment for selected vendor': 240, 'Promo New RFS Disc 15% Value30 Mbps Combo New': 241, 'Promo CLBK Disc 25% (12 Bulan) Fast50 Mbps New': 242, 'Promo CLBK Disc 25% (12 Bulan) Jet20 Mbps Combo New': 243, 'Promo CLBK Disc 25% (12 Bulan) Nova100 Mbps Combo New': 244, 'Promo CLBK Disc 25% (12 Bulan) Hype75 Mbps New': 245, 'Promo CLBK Disc 25% (12 Bulan) Business20 Mbps': 246, 'Promo New RFS Disc 25% Gamer150 Mbps New ': 247, 'Promo New RFS Disc 25% Fast50 Mbps Combo New': 248, 'Promo Disc 20% (12 Bulan) Business300 Mbps + TV': 249, 'Promo CLBK Disc 25% (12 Bulan) Gamer150 Mbps New': 250, 'Discount VIP NRO 2021 (6months)': 251, 'Promo Thamrin Residence Disc 20% (6 Bulan) Fast50 Combo A': 252, 'Promo Thamrin Residence Disc 20% (6 Bulan) Nova100 ': 253, 'Promo Disc 25% (12 Bulan) Fast50': 254, 'Promo Disc20% 12 Bulan MyGamer250 Combo A': 255, 'Promo Disc 25% (12 Bulan) Nova100': 256, 'Promo Disc 25% (12 Bulan) Nova100  Combo A': 257, 'Promo New RFS Lampung dan Pekanbaru  (Disc 25% 12 Bulan)  MyGamer250 Combo A': 258, 'Promo Disc 25% (12 Bulan) Hype75': 259, 'Promo Thamrin Residence MyGamer250 Mbps': 260, 'Promo Disc 15% (12 Bulan) Value30 Combo A': 261, 'Promo New RFS Lampung dan Pekanbaru  (Disc 25% 12 Bulan)  MyGamer250 Mbps': 262, 'Promo Merdeka Disc 25% 6 Bulan (MyGamer250 Combo A)': 263, 'Promo Disc 25% (12 Bulan) Business300 Mbps': 264, 'Promo CLBK Disc 25% (12 Bulan) Value30 Internet': 265, 'Promo CLBK Disc 25% (12 Bulan) Value30 Combo A': 266, 'Promo CLBK Disc 25% (12 Bulan) Business50 Mbps': 267, 'Promo Disc 25% (12 Bulan) Business50 Mbps': 268, 'Promo CLBK Disc 25% (12 Bulan) Hype75 Internet': 269, 'Promo Nasional (Disc 15% 6 Bulan) MyGamer250 Combo A': 270, 'Promo Thamrin Residence Disc 20% (6 Bulan) Hype75': 271, 'Promo Thamrin Residence MyGamer250 Combo A': 272, 'Promo Thamrin Residence Disc 20% (6 Bulan) Hype75 Combo A': 273, 'Promo CLBK Disc 25% (12 Bulan) MyGamer250 Internet': 274, 'Promo CLBK Disc 25% (12 Bulan) Nova100 Internet': 275, 'Promo New RFS HRB Disc 20% (6 Bulan) Nova100 ': 276, ' Promo Flash Sale 9.9 Value30 Internet ': 277, 'Promo Harbolnas September MyGamer250 Combo A': 278, 'Promo Harbolnas September Nova100 Combo A': 279, 'Promo New RFS HRB MyGamer250 Mbps': 280, 'Promo Oktober 2022 Disc 25% (12 Bulan) Nova100 Combo A': 281, 'Promo New RFS HRB Disc 20% (6 Bulan) Fast50 Combo A': 282, 'Promo CLBK Disc 25% (12 Bulan) MyGamer250 Combo A': 283, 'Discount VIP NRO (12months)': 284, 'Promo Oktober 2022 Disc 25% (12 Bulan) MyGamer250 Internet': 285, 'Promo Disc 25% (12 Bulan) Business100 Mbps': 286, 'Discount VIP NRO (24months)': 287, 'Discount VIP NRO (6months)': 288, 'Promo CLBK Disc 25% (12 Bulan) Fast50 Combo A': 289, 'Promo Disc 15% (12 Bulan) MyGamer250': 290, 'Promo Disc 20% (12 Bulan) Business100 Mbps + TV': 291, 'Discount VIP NRO (36months)': 292, 'Promo Internet VIP Rumah Ibadah': 293, 'Promo Oktober 2022 Disc 25% (12 Bulan) Fast50 Combo A': 294, 'Promo Oktober 2022 Disc 25% (12 Bulan) MyGamer250 Combo A': 295, 'Promo Ruko Special Price Disc 15% (6 Bulan) Jet20 Internet': 296, 'Promo Ruko Special Price Disc 15% (6 Bulan) Jet20 Combo A': 297, 'Promo Ruko Special Price Disc 15% (6 Bulan) Value30 Internet': 298, 'Promo Ruko Special Price Disc 15% (6 Bulan) FiberPro20': 299, 'Promo CLBK Disc 25% (12 Bulan) Nova100 Combo A': 300, 'Promo Ruko Special Price Disc 15% (6 Bulan) MyGamer250 Internet': 301, 'Promo Ruko Special Price Disc 15% (6 Bulan) Fast50 Internet': 302, 'Promo Disc 15% (12 Bulan) Business20 Mbps': 303, 'Promo Shocktober Disc 25% (12 Bulan) Jet20 Combo A': 304, 'Promo Shocktober Disc 30% (12 Bulan) Nova100 Internet': 305, 'Promo Shocktober Disc 30% (12 Bulan) MyGamer250 Internet': 306, 'Promo Shocktober Disc 30% (12 Bulan) Fast50 Combo A': 307, 'Promo Shocktober Disc 30% (12 Bulan) MyGamer250 Combo A': 308, 'Promo Ruko Special Price Disc 15% (6 Bulan) Nova100 Internet': 309, 'Promo Disc 25% (12 Bulan) Value30 Combo A': 310, 'Promo WOW-VEMBER DEALS Nova100 Internet': 311, 'Promo Disc 25% (12 Bulan) Value30': 312, 'Promo MyRep YES Value30 Combo A': 313, 'Promo New RFS HRB Disc 15% (6 Bulan) Nova100 Combo A': 314, 'Discount VIP NRO (3months)': 315, 'Promo New RFS HRB Disc 20% (6 Bulan) Nova100 Combo A': 316, 'Promo WOW FLASH SALE MyGamer250 Internet': 317, 'Promo WOW FLASH SALE Fast50 Internet': 318, 'Promo WOW FLASH SALE Nova100 Internet': 319, 'Promo WOW FLASH SALE Fast50 Combo A': 320, 'Promo WOW FLASH SALE Nova100 Combo A': 321, 'Promo WOW FLASH SALE MyGamer250 Combo A': 322, 'Promo WOW-VEMBER DEALS MyGamer250 Internet': 323, 'Promo WOW-VEMBER DEALS Nova100 Combo A': 324, 'Promo WOW-VEMBER DEALS MyGamer250 Combo A': 325, 'Promo Ruko Special Price Disc 15% (6 Bulan) FiberPro60': 326, 'Promo Akhir Tahun 2022 Disc 20% (12 Bulan) Nova100': 327, 'Promo MyRep YES Fast50 Internet': 328, 'Promo Disc 25% (12 Bulan) Business300 Mbps + TV': 329, 'Promo New RFS HRB Disc 15% (6 Bulan) Nova100 Internet': 330, 'Promo New RFS HRB Disc 20% (6 Bulan) MyGamer250 Mbps': 331, 'Promo Akhir Tahun 2022 Disc 20% (12 Bulan) Fast50': 332, 'Promo Akhir Tahun 2022 Disc 20% (12 Bulan) Fast50 Combo A': 333, 'Promo Akhir Tahun 2022 Disc 20% (12 Bulan) MyGamer250': 334, 'Promo Akhir Tahun 2022 Disc 20% (12 Bulan) MyGamer250 Combo A': 335, 'Promo HRB YES Disc 30% Fast50 Internet (3 Bulan)': 336, 'Promo HRB YES Disc 30% Value30 Internet (3 Bulan)': 337, 'Promo Disc 20% (12 Bulan) Advance Payment': 338, 'Promo MyRep YES Nova100 Internet': 339, 'Promo MyRep YES Fast50 Combo A': 340, 'Promo MyRep YES Nova100 Combo A': 341, 'Promo Disc 15% (12 Bulan) Advance Payment': 342, 'Promo MyRep YES MyGamer250 Internet': 343, 'Promo MyRep YES MyGamer250 Combo A': 344, 'Promo New Year New Value Internet': 345, 'Promo Disc 22%+12% (12 Bulan) Advance Payment': 346, 'Promo Akhir Tahun 2022 Disc 20% (12 Bulan) Nova100  Combo A': 347, 'Promo Nasional 2023 Disc. 15% (12 Bulan) Jet20': 348, 'Promo New RFS HRB Disc 15% (6 Bulan) MyGamer250 Internet': 349, 'Promo HRB YES Disc 30% MyGamer250 Combo A': 350, 'Promo HRB YES Disc 30% Nova100 Internet (3 Bulan)': 351, 'Promo HRB YES Disc 30% MyGamer250 Internet (3 Bulan)': 352, 'Promo HRB YES Disc 30% Fast50 Combo A': 353, 'Promo HRB YES Disc 30% Value30 Combo A': 354, 'Flash Sale Puri Casablanca Disc 50% (6 Bulan) MyGamer250 Internet': 355, 'Promo Disc 25% (12 Bulan) BusinessPro150 Mbps': 356, 'Promo New Year New Value Combo': 357, 'Promo Nasional 2023 Disc. 15% (12 Bulan) Value30': 358, 'Promo Disc 30% (12 Bulan) MyGamer250': 359, 'Promo Nasional 2023 Disc. 25% (12 Bulan) Nova100 Combo A': 360, 'Promo Nasional 2023 Disc. 20% (12 Bulan) Fast50': 361, 'Promo Nasional 2023 Disc. 15% (12 Bulan) Jet20 Combo A': 362, 'Promo Nasional 2023 Disc. 15% (12 Bulan) Value30 Combo A': 363, 'Promo Nasional 2023 Disc. 25% (12 Bulan) MyGamer250': 364, 'Promo Nasional 2023 Disc. 25% (12 Bulan) Nova100': 365, 'Promo New Year New Value (Advance Payment)': 366, 'Promo Nasional 2023 Disc. 25% (12 Bulan) MyGamer250 Combo A': 367, 'Promo Nasional 2023 Disc. 20% (12 Bulan) Fast50 Combo A': 368, 'Promo Nasional 2023 (PA 5 Get 1) Fast50 Combo Internet A': 369, 'Promo Nasional 2023 (PA 5 Get 1) Fast50': 370, 'Promo New RFS HRB Disc 15% (6 Bulan) Value30 Internet': 371, 'Promo Nasional 2023 (PA 5 Get 1) Jet20': 372, 'Promo Nasional 2023 (PA 5 Get 1) Value30': 373, 'Promo Disc 30% (12 Bulan) Nova100': 374, 'Promo Nasional 2023 (PA 5 Get 1) Nova100': 375, 'Promo Nasional 2023 (PA 5 Get 1) Value30 Combo Internet A': 376, 'Promo Nasional 2023 (PA 5 Get 1) MyGamer250': 377}

dict_churn = {"Churn" : 1, "Not Churn" : 0}

def preprocess_input(input_df):
    input_df['Area Name'] = input_df['Area Name'].map(area_dict)
    input_df['Plan'] = input_df['Plan'].map(plan_dict)
    input_df['Tv Plan'] = input_df['Tv Plan'].map(dict_tvplan)
    input_df['Advance Promo'] = input_df['Advance Promo'].map(dict_promo)

    return input_df

def reverse(df):
    inverse_dict_areaname = {v: k for k, v in area_dict.items()}
    inverse_dict_plan = {v: k for k, v in plan_dict.items()}
    inverse_dict_tvplan = {v: k for k, v in dict_tvplan.items()}
    inverse_dict_promo = {v: k for k, v in dict_promo.items()}
    inverse_dict_churn = {v: k for k, v in dict_churn.items()}

    df['Area Name'] = df['Area Name'].map(inverse_dict_areaname)
    df['Plan'] = df['Plan'].map(inverse_dict_plan)
    df['Tv Plan'] = df['Tv Plan'].map(inverse_dict_tvplan)
    df['Advance Promo'] = df['Advance Promo'].map(inverse_dict_promo)
    df['Churn'] = df['Churn'].map(inverse_dict_churn)

    return(df)

def predict_churn(data):
    data = preprocess_input(data)
    predictions = model.predict(data)
    data["Churn"] = predictions
    data = reverse(data)

    return data

def load_churned(data):
    data = data[data['Churn'] == 'Churn']
    # Area Name
    unique_values_area_churned = data['Area Name'].unique()
    count_area_churned = data['Area Name'].value_counts()[unique_values_area_churned]
    area_data_churned = pd.DataFrame({'Area Name': unique_values_area_churned, 'Count': count_area_churned})

    # Plan
    unique_values_plan_churned = data['Plan'].unique()
    count_plan_churned = data['Plan'].value_counts()[unique_values_plan_churned]
    plan_data_churned = pd.DataFrame({'Plan': unique_values_plan_churned, 'Count': count_plan_churned})

    # Tv Plan
    unique_values_tvplan_churned = data['Tv Plan'].unique()
    count_tvplan_churned = data['Tv Plan'].value_counts()[unique_values_tvplan_churned]
    tvplan_data_churned = pd.DataFrame({'Tv Plan': unique_values_tvplan_churned, 'Count': count_tvplan_churned})

    # Advance Promo
    unique_values_adv_churned = data['Advance Promo'].unique()
    count_adv_churned = data['Advance Promo'].value_counts()[unique_values_adv_churned]
    adv_data_churned = pd.DataFrame({'Advance Promo': unique_values_adv_churned, 'Count': count_adv_churned})

    # Complaint by Customer Service
    unique_values_com_cs_churned = data['Complaint by Customer Service'].unique()
    count_com_cs_churned = data['Complaint by Customer Service'].value_counts()[unique_values_com_cs_churned]
    com_cs_data_churned = pd.DataFrame({'Complaint by Customer Service': unique_values_com_cs_churned, 'Count': count_com_cs_churned})

    # Complaint by Email
    unique_values_com_e_churned = data['Complaint by Email'].unique()
    count_com_e_churned = data['Complaint by Email'].value_counts()[unique_values_com_e_churned]
    com_e_data_churned = pd.DataFrame({'Complaint by Email': unique_values_com_e_churned, 'Count': count_com_e_churned})

    # Complaint by Social Media
    unique_values_com_socmed_churned = data['Complaint by Social Media'].unique()
    count_com_socmed_churned = data['Complaint by Social Media'].value_counts()[unique_values_com_socmed_churned]
    com_socmed_data_churned = pd.DataFrame({'Complaint by Social Media': unique_values_com_socmed_churned, 'Count': count_com_socmed_churned})

    # Complaint by Telegram
    unique_values_tele_churned = data['Complaint by Telegram'].unique()
    count_tele_churned = data['Complaint by Telegram'].value_counts()[unique_values_tele_churned]
    tele_data_churned = pd.DataFrame({'Complaint by Telegram': unique_values_tele_churned, 'Count': count_tele_churned})

    # Complaint by Whatsapp
    unique_values_wa_churned = data['Complaint by Whatsapp'].unique()
    count_wa_churned = data['Complaint by Whatsapp'].value_counts()[unique_values_wa_churned]
    wa_data_churned = pd.DataFrame({'Complaint by Whatsapp': unique_values_wa_churned, 'Count': count_wa_churned})

    # Complaint by WIC
    unique_values_wic_churned = data['Complaint by WIC'].unique()
    count_wic_churned = data['Complaint by WIC'].value_counts()[unique_values_wic_churned]
    wic_data_churned = pd.DataFrame({'Complaint by WIC': unique_values_wic_churned})

    return area_data_churned, plan_data_churned, tvplan_data_churned, \
           adv_data_churned, com_cs_data_churned, com_e_data_churned, \
           com_socmed_data_churned, tele_data_churned, wa_data_churned, wic_data_churned


def load_non_churned(data):
    data = data[data['Churn'] == 'Not Churn']
    # Area Name
    unique_values_area_non_churned = data['Area Name'].unique()
    count_area_non_churned = data['Area Name'].value_counts()[unique_values_area_non_churned]
    area_data_non_churned = pd.DataFrame({'Area Name': unique_values_area_non_churned, 'Count': count_area_non_churned})

    # Plan
    unique_values_plan_non_churned = data['Plan'].unique()
    count_plan_non_churned = data['Plan'].value_counts()[unique_values_plan_non_churned]
    plan_data_non_churned = pd.DataFrame({'Plan': unique_values_plan_non_churned, 'Count': count_plan_non_churned})

    # Tv Plan
    unique_values_tvplan_non_churned = data['Tv Plan'].unique()
    count_tvplan_non_churned = data['Tv Plan'].value_counts()[unique_values_tvplan_non_churned]
    tvplan_data_non_churned = pd.DataFrame({'Tv Plan': unique_values_tvplan_non_churned, 'Count': count_tvplan_non_churned})

    # Advance Promo
    unique_values_adv_non_churned = data['Advance Promo'].unique()
    count_adv_non_churned = data['Advance Promo'].value_counts()[unique_values_adv_non_churned]
    adv_data_non_churned = pd.DataFrame({'Advance Promo': unique_values_adv_non_churned, 'Count': count_adv_non_churned})

    # Complaint by Customer Service
    unique_values_com_cs_non_churned = data['Complaint by Customer Service'].unique()
    count_com_cs_non_churned = data['Complaint by Customer Service'].value_counts()[unique_values_com_cs_non_churned]
    com_cs_data_non_churned = pd.DataFrame({'Complaint by Customer Service': unique_values_com_cs_non_churned, 'Count': count_com_cs_non_churned})

    # Complaint by Email
    unique_values_com_e_non_churned = data['Complaint by Email'].unique()
    count_com_e_non_churned = data['Complaint by Email'].value_counts()[unique_values_com_e_non_churned]
    com_e_data_non_churned = pd.DataFrame({'Complaint by Email': unique_values_com_e_non_churned, 'Count': count_com_e_non_churned})

    # Complaint by Social Media
    unique_values_com_socmed_non_churned = data['Complaint by Social Media'].unique()
    count_com_socmed_non_churned = data['Complaint by Social Media'].value_counts()[unique_values_com_socmed_non_churned]
    com_socmed_data_non_churned = pd.DataFrame({'Complaint by Social Media': unique_values_com_socmed_non_churned, 'Count': count_com_socmed_non_churned})

    # Complaint by Telegram
    unique_values_tele_non_churned = data['Complaint by Telegram'].unique()
    count_tele_non_churned = data['Complaint by Telegram'].value_counts()[unique_values_tele_non_churned]
    tele_data_non_churned = pd.DataFrame({'Complaint by Telegram': unique_values_tele_non_churned, 'Count': count_tele_non_churned})

    # Complaint by Whatsapp
    unique_values_wa_non_churned = data['Complaint by Whatsapp'].unique()
    count_wa_non_churned = data['Complaint by Whatsapp'].value_counts()[unique_values_wa_non_churned]
    wa_data_non_churned = pd.DataFrame({'Complaint by Whatsapp': unique_values_wa_non_churned, 'Count': count_wa_non_churned})

    # Complaint by WIC
    unique_values_wic_non_churned = data['Complaint by WIC'].unique()
    count_wic_non_churned = data['Complaint by WIC'].value_counts()[unique_values_wic_non_churned]
    wic_data_non_churned = pd.DataFrame({'Complaint by WIC': unique_values_wic_non_churned, 'Count': count_wic_non_churned})

    return area_data_non_churned, plan_data_non_churned, tvplan_data_non_churned, adv_data_non_churned, com_cs_data_non_churned, com_e_data_non_churned, com_socmed_data_non_churned, tele_data_non_churned, wa_data_non_churned, wic_data_non_churned


def visualize_data_batch(data):
    pdf_path = "Churn Predict.pdf"
    pdf_pages = PdfPages(pdf_path)
    
    st.header("Hasil Prediksi")
    # st.table(data)
    st.table(data.head(10))

    # Menampilkan tombol "Download File CSV"
    if st.button('Download Here - All Data', key='download_all'):
        csv_data = data.to_csv(index=False)
        href = f'<a href="data:file/csv;charset=utf-8,{csv_data}" download="data.csv">Download File CSV</a>'
        st.markdown("Untuk mendownload file seluruh:")
        st.markdown(href, unsafe_allow_html=True)

    st.header("Churn Distribution")
    fig, ax = plt.subplots()
    palette_color = sns.color_palette('rocket_r')

    churn_counts = data['Churn'].value_counts()
    ax = churn_counts.plot(kind='pie', autopct='%1.1f%%', colors=palette_color)
    ax.set_ylabel('')

    ax.legend(churn_counts.index)
    
    # Mengatur judul di tengah pie chart
    ax.set_title("Churn Distribution", loc='center')

    st.pyplot(fig)
    churn_counts = data['Churn'].value_counts()
    total_churn = churn_counts['Churn']
    total_not_churn = churn_counts['Not Churn']

    data_counts = pd.DataFrame({'Jenis Churn': ['Churn', 'Not Churn'],
                            'Jumlah Data': [total_churn, total_not_churn]})

    data_counts['Persentase'] = data_counts['Jumlah Data'].apply(lambda x: f"{(x / data.shape[0]) * 100:.2f}%")

    st.table(data_counts)
    pdf_pages.savefig(fig)

    data_churned = data[data['Churn'] == 'Churn']
    st.header('Churned Data')
    st.table(data_churned.head(10))

    # Menampilkan tombol "Download File CSV"
    if st.button('Download Here - Churned Data', key='download_churned'):
        csv_data_churned = data_churned.to_csv(index=False)
        href_churned = f'<a href="data:file/csv;charset=utf-8,{csv_data_churned}" download="data_churned.csv">Download File CSV</a>'
        st.markdown("Untuk mendownload file seluruh:")
        st.markdown(href_churned, unsafe_allow_html=True)

    data_not_churned = data[data['Churn'] == 'Not Churn']
    st.header('Not Churned Data')
    st.table(data_not_churned.head(10))

    # Menampilkan tombol "Download File CSV"
    if st.button('Download Here - Not Churned Data', key='download_not_churned'):
        csv_data_not_churned = data_not_churned.to_csv(index=False)
        href_not_churned = f'<a href="data:file/csv;charset=utf-8,{csv_data_not_churned}" download="data_not_churned.csv">Download File CSV</a>'
        st.markdown("Untuk mendownload file seluruh:")
        st.markdown(href_not_churned, unsafe_allow_html=True)

    # Menghitung jumlah data Churn ##BARUU 18 JULI 2023
    churn_data = data[data['Churn'] == 'Churn']
    churn_counts = churn_data.shape[0]

    # Menghitung persentase komposisi data Churn pada setiap kolom data
    churn_composition = churn_data.apply(lambda x: (x.value_counts() / churn_counts) * 100)

    # Menampilkan jumlah data dan persentase komposisi data Churn pada setiap kolom data
    st.header("Data Churn")
    st.subheader("Jumlah Data Churn")
    st.table(churn_data.count())

    st.subheader("Persentase Komposisi Data Churn")
    st.table(churn_composition)

    # Menghitung jumlah data Not Churn
    not_churn_data = data[data['Churn'] == 'Not Churn']
    not_churn_counts = not_churn_data.shape[0]

    # Menghitung persentase komposisi data Not Churn pada setiap kolom data
    not_churn_composition = not_churn_data.apply(lambda x: (x.value_counts() / not_churn_counts) * 100)

    # Menampilkan jumlah data dan persentase komposisi data Not Churn pada setiap kolom data
    st.header("Data Not Churn")
    st.subheader("Jumlah Data Not Churn")
    st.table(not_churn_data.count())

    st.subheader("Persentase Komposisi Data Not Churn")
    st.table(not_churn_composition)
    
    
    area_data_churned, plan_data_churned, tvplan_data_churned, \
    adv_data_churned, com_cs_data_churned, com_e_data_churned, \
    com_socmed_data_churned, tele_data_churned, wa_data_churned, wic_data_churned = load_churned(data)

    area_data_non_churned, plan_data_non_churned, tvplan_data_non_churned, \
    adv_data_non_churned, com_cs_data_non_churned, com_e_data_non_churned, \
    com_socmed_data_non_churned, tele_data_non_churned, wa_data_non_churned, wic_data_non_churned = load_non_churned(data)

    #Area Data Churned
    area_data_churned = area_data_churned.reset_index(drop=True)
    st.table(area_data_churned)
    data = data[data["Churn"] == "Churn"]
    columns = data.columns.to_list()
    
    #Area Name
    palette_area = sns.color_palette('crest')

    top_val = data["Area Name"].value_counts().nlargest(5)
    fig = plt.figure(figsize=(10, 5))
    sns.barplot(x=data["Area Name"].value_counts().values, y=top_val.index, palette=palette_area)
    plt.title(f"Top 10 Area Name - Churned")
    plt.xlabel("Total Customer")
    plt.ylabel("Area Name")

    # Membuat legenda dengan warna yang sama
    handles = [plt.Rectangle((0, 0), 1, 1, fc=palette_area[i % len(palette_area)]) for i in range(len(top_val.index))]
    labels = [value for value in top_val.index]
    plt.legend(handles, labels)

    plt.grid(False)
    pdf_pages.savefig(fig)
    st.pyplot(fig)

    #Plan
    palette_plan = sns.color_palette('flare')

    top_val = data["Plan"].value_counts().nlargest(5)
    fig = plt.figure(figsize=(10, 5))
    sns.barplot(x=data["Plan"].value_counts().values, y=top_val.index, palette=palette_plan)
    plt.title(f"Top 10 Plan - Churned")
    plt.xlabel("Total Customer")
    plt.ylabel("Plan")

    # Membuat legenda dengan warna yang sama
    handles = [plt.Rectangle((0, 0), 1, 1, fc=palette_plan[i % len(palette_plan)]) for i in range(len(top_val.index))]
    labels = [value for value in top_val.index]
    plt.legend(handles, labels)

    plt.grid(False)
    pdf_pages.savefig(fig)
    st.pyplot(fig)

    #TV Plan
    palette_tvplan = sns.color_palette(["#43C6AC", "#F8FFAE"], n_colors=10)

    top_val = data["Plan"].value_counts().nlargest(5)
    fig = plt.figure(figsize=(10, 5))
    sns.barplot(x=data["Plan"].value_counts().values, y=top_val.index, palette=palette_tvplan)
    plt.title(f"Top 10 Plan - Churned")
    plt.xlabel("Total Customer")
    plt.ylabel("Plan")

    # Membuat legenda dengan warna yang sama
    handles = [plt.Rectangle((0, 0), 1, 1, fc=palette_tvplan[i % len(palette_tvplan)]) for i in range(len(top_val.index))]
    labels = [value for value in top_val.index]
    plt.legend(handles, labels)

    plt.grid(False)
    pdf_pages.savefig(fig)
    st.pyplot(fig)


    #Advance Promo
    palette_advpromo = sns.color_palette(["#000C40", "#F0F2F0"], n_colors=10)

    top_val = data["Plan"].value_counts().nlargest(5)
    fig = plt.figure(figsize=(10, 5))
    sns.barplot(x=data["Plan"].value_counts().values, y=top_val.index, palette=palette_advpromo)
    plt.title(f"Top 10 Plan - Churned")
    plt.xlabel("Total Customer")
    plt.ylabel("Plan")

    # Membuat legenda dengan warna yang sama
    handles = [plt.Rectangle((0, 0), 1, 1, fc=palette_advpromo[i % len(palette_advpromo)]) for i in range(len(top_val.index))]
    labels = [value for value in top_val.index]
    plt.legend(handles, labels)

    plt.grid(False)
    pdf_pages.savefig(fig)
    st.pyplot(fig)
    
    #Complaint by Customer Service
    fig = plt.figure(figsize=(10, 5))
    top_val = data["Complaint by Customer Service"].value_counts().nlargest(10)

    palette_cs = sns.color_palette(["#C5796D", "#DBE6F6"], n_colors=10)
    ax = sns.countplot(x="Complaint by Customer Service", data=data, order=top_val.index, palette=palette_cs)

    # Setting title, labels, and grid
    plt.title(f"Top 10 Complaint by Customer Service - Churned")
    plt.xlabel("Value")
    plt.ylabel("Count")
    plt.grid(False)

    # Membuat legenda dengan warna yang sama
    handles = [plt.Rectangle((0, 0), 1, 1, fc=palette_cs[i]) for i in range(len(top_val.index))]
    labels = [value for value in top_val.index]
    plt.legend(handles, labels)
    plt.grid(False)

    pdf_pages.savefig(fig)
    st.pyplot(fig)

    #Complaint by Email
    fig = plt.figure(figsize=(10, 5))
    top_val = data["Complaint by Email"].value_counts().nlargest(10)

    palette_e = sns.color_palette(["#67B26F", "#4ca2cd"], n_colors=10)
    ax = sns.countplot(x="Complaint by Email", data=data, order=top_val.index, palette=palette_e)

    # Setting title, labels, and grid
    plt.title(f"Top 10 Complaint by Email - Churned")
    plt.xlabel("Value")
    plt.ylabel("Count")
    plt.grid(False)

    # Membuat legenda dengan warna yang sama
    handles = [plt.Rectangle((0, 0), 1, 1, fc=palette_e[i]) for i in range(len(top_val.index))]
    labels = [value for value in top_val.index]
    plt.legend(handles, labels)
    plt.grid(False)

    pdf_pages.savefig(fig)
    st.pyplot(fig)

    #Complaint by Social Media
    fig = plt.figure(figsize=(10, 5))
    top_val = data["Complaint by Social Media"].value_counts().nlargest(10)

    palette_sm = sns.color_palette(["#F3904F", "#3B4371"], n_colors=10)
    ax = sns.countplot(x="Complaint by Social Media", data=data, order=top_val.index, palette=palette_sm)

    # Setting title, labels, and grid
    plt.title(f"Top 10 Complaint by Social Media - Churned")
    plt.xlabel("Value")
    plt.ylabel("Count")
    plt.grid(False)

    # Membuat legenda dengan warna yang sama
    handles = [plt.Rectangle((0, 0), 1, 1, fc=palette_sm[i]) for i in range(len(top_val.index))]
    labels = [value for value in top_val.index]
    plt.legend(handles, labels)
    plt.grid(False)

    pdf_pages.savefig(fig)
    st.pyplot(fig)

    #Complaint by Telegram
    fig = plt.figure(figsize=(10, 5))
    top_val = data["Complaint by Telegram"].value_counts().nlargest(10)

    palette_tele = sns.color_palette(["#A770EF", "#CF8BF3", "#FDB99B"], n_colors=10)
    ax = sns.countplot(x="Complaint by Telegram", data=data, order=top_val.index, palette=palette_tele)

    # Setting title, labels, and grid
    plt.title(f"Top 10 Complaint by Telegram - Churned")
    plt.xlabel("Value")
    plt.ylabel("Count")
    plt.grid(False)

    # Membuat legenda dengan warna yang sama
    handles = [plt.Rectangle((0, 0), 1, 1, fc=palette_tele[i]) for i in range(len(top_val.index))]
    labels = [value for value in top_val.index]
    plt.legend(handles, labels)
    plt.grid(False)

    pdf_pages.savefig(fig)
    st.pyplot(fig)

    #Complaint by Whatsapp
    fig = plt.figure(figsize=(10, 5))
    top_val = data["Complaint by Whatsapp"].value_counts().nlargest(10)

    palette_wa = sns.color_palette(["#FF00CC", "#333399"], n_colors=10)
    ax = sns.countplot(x="Complaint by Whatsapp", data=data, order=top_val.index, palette=palette_wa)

    # Setting title, labels, and grid
    plt.title(f"Top 10 Complaint by Whatsapp - Churned")
    plt.xlabel("Value")
    plt.ylabel("Count")
    plt.grid(False)

    # Membuat legenda dengan warna yang sama
    handles = [plt.Rectangle((0, 0), 1, 1, fc=palette_wa[i]) for i in range(len(top_val.index))]
    labels = [value for value in top_val.index]
    plt.legend(handles, labels)
    plt.grid(False)

    pdf_pages.savefig(fig)
    st.pyplot(fig)

    #Complaint by WIC
    fig = plt.figure(figsize=(10, 5))
    top_val = data["Complaint by WIC"].value_counts().nlargest(10)

    palette_wic = sns.color_palette(["#BE93C5", "#7BC6CC"], n_colors=10)
    ax = sns.countplot(x="Complaint by WIC", data=data, order=top_val.index, palette=palette_wic)

    # Setting title, labels, and grid
    plt.title(f"Top 10 Complaint by WIC - Churned")
    plt.xlabel("Value")
    plt.ylabel("Count")
    plt.grid(False)

    # Membuat legenda dengan warna yang sama
    handles = [plt.Rectangle((0, 0), 1, 1, fc=palette_wic[i]) for i in range(len(top_val.index))]
    labels = [value for value in top_val.index]
    plt.legend(handles, labels)
    plt.grid(False)

    pdf_pages.savefig(fig)
    st.pyplot(fig)

    pdf_pages.close()
    st.success("PDF Report Created. Check your directory")

def run():
    add_selectbox = st.sidebar.selectbox(
        "How would you like to predict?",
        ("Online", "Batch","About"))
    st.sidebar.info('This app is created to customer churn prediction')
    st.title("Customer Churn Prediction")
    
    # Menentukan nama kolom yang diharapkan
    expected_columns = ['Area Name', 'Plan', 'Tv Plan', 'Advance Promo', 'Complaint by Customer Service', 'Complaint by Email', 'Complaint by Social Media', 'Complaint by Telegram', 'Complaint by Whatsapp', 'Complaint by WIC']

    if add_selectbox == 'Online':        
        user_area = st.selectbox('Area Name', 
                                        ('Tangerang', 'Depok', 'Cibubur', 'Bekasi', 'Surabaya',
                                         'Semarang', 'Bogor', 'Malang', 'Palembang', 'Jakarta', 'Medan',
                                         'Bandung', 'Bali', 'Makassar','Serang', 'Pekanbaru', 'Lampung',
                                         'Solo', 'Cilegon', 'Karawang', 'Jambi')
                                        )
        user_plan = st.selectbox('Plan', 
                                 ('Tanpa Plan', 'Value30 Mbps', 'Fast50 Mbps', 'Fast-50 Super93 (1x)', 'Fast50 (PI21-C)', 'Value30 (PI20-B)', 'Nova-100 Super93 (1x)', 'Nova100 (PI20-B)','Gamer150 (PI20-B)', 'Fast-50 Super93 (2x)', 'Value30 (PI20-A)', 'Value30 Mbps New', 'Fast50 (PI21-A)', 'Value30 (PI21-B)', 'Fast50 (PI20-B)', 'Nova100 Mbps Lite', 'Value30 Mbps (PA)', 'Nova100 (PI21-B)', 'Fast50 Mbps New', 'Gamer-150 Super93 (2x)', 'Value-30 Super93 (2x)', 'Fast50 (PI21-D)', 'SNAP (Internet Up To 10 Mbps)', 'Value-30 Super93 (1x)', 'BLITZ (Internet Up To 20 Mbps)', 'Fast50 (PI20-A)', 'Hype75 Mbps New', 'Fast50 Special', 'Nova100 Mbps Lite (PA)', 'Nova150 (PI21-B)', 'Value30 (PI21-E)', 'Fast50 Combo', 'Fast.50', 'Gamer 150 Mbps+', 'Gamer50 (PI20-A)', 'Gamer150 Mbps', 'Fast50 (PI21-B)', 'Value30 (PI21-A)', 'Gamer150 (PI21-B)', 'Nova100 (PI20-A)', 'Value30', 'Gamer-150 Super93 (1x)', 'Jet-20 - winback', 'Jet20 (PI20-A)', 'Jet20 Mbps New', 'Nova150 (PI21-A)', 'Nova-100', 'Fast50 (PI21-E)', 'Nova100 (PI21-D)', 'Gamer150 (PI20-A)', 'Hype75 Combo New', 'Fast 50 Mbps+', 'Fast50 Combo New', 'Value-30', 'EazyNet (Bonus TV)', 'Rapid', 'FUN (10 Mbps + TV SD & HD Channels)', 'Jet20 (PI20-B)', 'FUN Promo', 'Nova-100 Super93 (2x)', 'Fast50 Mbps (PA)', 'Nova100 Mbps', 'Jet20 (PI21-A)', 'Value 30 Mbps+', 'Jet20 Internet', 'Nova100+', 'Business 50 (PI20)', 'Gamer150 Mbps Reg', 'SuperNova300 (PI-21)', 'Business 100 (PI20)', 'Magic Wifi 200 (PI21)', 'Gamer150 (PI21-D)', 'Nova 100 Mbps+', 'Value30 Internet', 'Nova100 Combo New', 'SuperNova300+', 'SuperNova-300', 'Value30 Combo', 'Nova100 (PI21-A)', 'Retain 10Mbps', 'Business 300 (PI20)', 'Gamer150 Combo', 'Gamer50', 'Business Pro 150  (PI20)', 'Basic30+', 'MyGamer250 Mbps', 'Business 50 (PI21)', 'Gamer50 (PI21-A)', 'GamerX50', 'Nova100 Special', 'Nova100 Combo (PA)', 'Business 100 Mbps (free installation fee)', 'Business.50 Mbps Reg', 'Gamer-150', 'Business 20 (PI20)', 'Value30 (PI21-D)', 'Fast50 Internet (PA)', 'Business 50 Mbps', 'Basic 30 Mbps', 'Business 30 Mbps (free installation fee)', 'Nova.100+', 'Fast-50', 'Fast50+', 'IBS.CA-Fiber120+ (PI-21)', 'Nova100 Mbps Reg', 'FiberPro 120', 'Business 300 (PI21)', 'Fast50 Internet', 'Nova100 Combo Internet A', 'Business 100 (PI21)', 'Business Pro 150 (PI21)', 'Business 100 Mbps (Promo Buy 1 Get 1)', 'IBS.CA-Fiber60+ (PI-21)', 'Value30 (PI21-C)', 'Nova150 Special 2', 'Business 20 Mbps', 'FiberPro 60 (PI-21)', 'Value30 Special 2' 'Basic8', 'IBS.CA Business30 (PI-21)', 'IBS.CA-Fiber60+', 'Business 20 (PI21)', 'Gamer150 Mbps New', 'Nova100 (PI21-C)', 'Business Pro 500 (PI20)', 'Basic15+', 'Hype75 Internet' 'Business 100 Mbps', 'Nova150 Special', 'IBS.CA Roket100 (PI-21)', 'Business 30 Mbps', 'Nova 100 Mbps+ XTRA', 'Fast50 Special 2', 'IBS.CA Business30', 'Gamer150 Mbps Reg (PA)', 'Value30 Combo New', 'Business 300 Mbps', 'FiberPro 20', 'Fast50 Combo (PA)', 'Gamer150 Combo (PA)', 'Business.300 Mbps Reg', 'Value30 Special', 'Jet-20', 'Jet20 Combo New', 'Jet20 Mbps', 'Gamer150 (PI21-A)', 'Jet20 Combo', 'Jet20', 'Nova100 Mbps New', 'Jet20 (PI21-D)', 'Business Pro 150 Mbps', 'Gamer-150 (fs)', 'Business Pro 500 Mbps', 'Alpha 10 Mbps', 'GAMER150+', 'Business50 Mbps (PA)', 'Nova100 Combo', 'Jet20 Lite', 'FiberPro 120 (PI-21)', 'IBS.CA Business 50 Mbps (PI-21)', 'Value30 Combo (PA)', 'Fast50 Mbps+ Xtra ComboTV', 'FiberPro 20 (PI-21)', 'Gamer-150 (smt)', 'Jet20 (PI21-C)', 'Fast-50 (fs)', 'Fast50 Combo Internet A', 'Value-30 (bit)', 'Fast-50 (smt)', 'Business Pro 500 (PI21)', 'Value-30 (fs)', 'Nova-100 (fs)', 'Value-30 (smt)', 'Hype75 Combo Internet A', 'FiberPro 60', 'Jet 20 PLUS', 'Value30 Mbps+ Xtra ComboTV', 'Jet20 (PI21-B)', 'Jet 20 PLUS AP12', 'Nova-100 (smt)', 'Gamer 150 Mbps+ Xtra ComboTV', 'Nova-100 (bit)', 'Jet 20 PLUS AP6', 'Gamer150 (PI21-C)', 'BusinessPro.150 Mbps Reg', 'Magic Wifi 200', 'Jet 20 Mbps+', 'Value30 Combo Internet A', 'Nova100 Internet', 'Gamer 75 Mbps+', 'Nova100 Mbps Reg (PA)', 'Jet 20 Mbps+ HITS', 'Fast 50 Mbps+ XTRA', 'Value 30 Mbps+ XTRA', 'Gamer 150 Mbps+ XTRA', 'Value 30 Mbps+ HITS', 'Gamer150 Mbps New (PA)', 'Gamer150 Combo New', 'Fast-50 (bit)', 'Jet20 Mbps+ Xtra ComboTV', 'Nova 100 Mbps+ Xtra ComboTV', 'Gamer 75 Mbps+ XTRA', 'Gamer 75 Mbps+ Xtra ComboTV', 'SuperNova-300 (fs)', 'IBS.CA Business 50 Mbps', 'IBS.CA Business Pro 150 Mbps', 'Nova 100 Mbps+ HITS', 'Fast 50 Mbps+ HITS', 'Value30 New (PA)', 'Sonic150 Combo', 'Flash75 ComboTV Pakubuwono', 'Gamer150 ComboTV Pakubuwono', 'Supernova300 ComboTV Pakubuwono', 'IBS.CA Business20', 'Fast50 Via Alma', 'Gamer200 Mbps Pakubuwono', 'IBS.CA Business300', 'Jet20 Mbps (PA)', 'Business20 Mbps (PA)', 'Jet20 Combo (PA)', 'Business100 Mbps (PA)', 'FiberPro 300', 'Business300 Mbps (PA)', 'BusinessPro 150 Mbps (PA)', 'Value30 Internet (PA)', 'VIP NRO 2021', 'Nova100 Mbps Pakubuwono', 'VIP NRO 2021 (FS)', 'BusinessPro 500 Mbps (PA)', 'VIP NRO 2021+', 'IBS.CA Business100', 'Value30 Combo New (PA)', 'Nova100 Mbps New (PA)', 'Hype75 Mbps New (PA)', 'Fast50 Mbps New (PA)', 'Jet20 Combo Internet A', 'Fast50 Combo New (PA)', 'Gamer150 Combo New (PA)', 'Fast50 Internet (AP77)', 'Value30 Internet (AP77)', 'MyGamer250 Internet (AP77)', 'Nova 100 Internet (AP77)', 'Value30 Combo Internet A (AP77)', 'MyGamer250 Combo Internet A', 'Hype75 Combo Internet A (PA)', 'Nova 100 Internet (PA)', 'Value30 Combo Internet A (PA)', 'Fast50 Combo Internet A (PA 12 Get 6)', 'MyGamer250 Combo Internet A (PA 12 Get 6)', 'MyGamer250 Mbps Internet (PA)', 'Value30 (PI-22F)', 'Nova100 (PI-22I)', 'Fast50 (PI-22H)', 'Nova100 (PI-22B)', 'Gamer150 (PI-22C)', 'Fast50 (PI-22I)', 'BSD Value (100 Mbps + TV)', 'Value30 (PI-22M)', 'Nova100 Combo Internet A (PA)', 'BSD Smash (300 Mbps + TV)', 'MyGamer250 Combo Internet A (PA)', 'Gamer150 (PI-22D)', 'VALUE PROMO', 'Value30 (PI-22H)', 'VALUE SUPER (Internet Up To 1 Mbps + TV Channel)', 'Nova100 (PI-22E)', 'Fast50 (PI-22G)', 'Snap Plus (Bonus TV)', 'Package Internet Up To 10 Mbps & TV Starter 15+', 'Value30 (PI-22G)', 'Fast50 Combo Internet A (PA)', 'BSD Basic 10 Mbps', 'Fast50 (PI-22C)', 'Basic Plus Star', 'Value30 (PI-22I)', 'Nova Plus Cosmic', 'Basic Plus Cosmic', 'Value30 (PI-22K)', 'BASIC SUPER (Internet Up To 512 Kbps + TV Channel)', 'Nova100 (PI-22J),' 'AMAZING (50 Mbps + TV SD & HD Channels)', 'BSD Pro 300 Mbps', 'Nova100 (PI-22H)', 'Bright', 'Gamer50 (PI-22C)', 'Value30 (PI-22J)', 'Value30 (PI-22N)', 'Hype75 (PI-22A)', 'Gamer150 (PI-22A)', 'Gamer150 (PI-22B)', 'Nova100 (PI-22L)', 'Nova150 (PI-22A)', 'Fast50 (PI-22B)', 'Nova150 (PI-22B)', 'Nova100 (PI-22D)', 'Lite (Package Internet Up To 3 Mbps & TV)', 'FESTIVE (40 Mbps + TV SD & HD Channels)', 'Internet Up To 512 Kbps', 'Internet Up To 3 Mbps', 'SuperNova Package', 'Value30 (PI-22C)', 'Gamer150+ XTRA (PI-22A)', 'Nova100 (PI-22C)', 'Fast50 (PI-22A)', 'Value30 Combo (PI-22B)', 'SUPER (20 Mbps + TV SD & HD Channels) KOWIS LEWIS', 'Jet20 (PI-22G)', 'XTREME (100 Mbps + TV SD & HD Channels)', 'Supernova300 Mbps (PA)', 'Value30 (PI-22D)', 'Fast50 Combo (PI-22A)', 'Jet20 (PI-22E)', 'Jet20 (PI-22A)', 'Fast50 Combo (PI-22C)', 'Nova100 (PI-22M)', 'Nova100 Combo (PI-22B)', 'Jet20 (PI-22K)', 'SUPER Promo' 'Fast50 (PI-22E)', 'Jet20 (PI-22C)', 'Fast50 (PI-22D)', 'Fast50 Combo (PI-22B)', 'Nova100 (PI-22G)', 'Business100 (PI-22B)', 'Business20 (PI-22B)','Fast50 (PI-22K)', 'Business300 (PI-22C)', 'Fast50 (PI-22F)' 'Basic15', 'Business50 (PI-22C)', 'Jet20 (PI-22D)', 'Value30 (PI-22A)', 'Nova100 Combo (PI-22A)', 'Basic (promo tv booster)', 'Gamer (promo tv booster)', 'Value30 (PI-22E)', 'Starter 6 Mbps', 'Fast50 (PI-22J)', 'BusinessPro150 (PI-22D)', 'Business50 (PI-22B)', 'Business100 (PI-22A)', 'Business300 (PI-22B)', 'Nova100 (PI-22F)', 'Gamer50 (PI-22A)', 'Business20 (PI-22A)', 'GamerX.50+', 'Nova (promo tv booster)', 'Fast50 (PI-22L)', 'MyGamer250 Combo Internet A (PA 12 Get 12)', 'Nova Package', 'Business 10 Mbps (free installation fee)', 'Value30 Combo (PI-22A)', 'Nova Plus Star', 'Business50 (PI-22A)', 'Nova Plus Star (diskon 25% 12 bulan)', 'Business 10 Mbps', 'GAMERX50+', 'Nova100 (PI-22A)', 'BusinessPro150 (PI-22C)', 'Business300 (PI-22A)', 'BusinessPro150 (PI-22B)', 'IBS.CA Roket100', 'IBS.CA-Fiber120+', 'Business 300 Mbps (Promo Buy 1 Get 1)', 'Basic.15+', 'GAMER.150+', 'IBS.CA Business300 (PI-21)', 'Business 300 Mbps (free installation fee)', 'Retain 10Mbps AdvanceTV', 'Basic.8+', 'IBS.CA Business100 (PI-21)', 'Jet20 Combo (PI-22A)', 'Business Pro 100 Mbps', 'FiberPro 300 (PI-21)', 'MyGamer250 Internet (PA 12 Get 12)', 'Value30 (PI-22B)', 'Nova100 Combo New (PA)', 'Value30 Internet (PA 12 Get 12)', 'Fast 50 Mbps', 'Hype75 Combo New (PA)', 'Gamer50 (PI-22B)', 'Business 75 (PI20)', 'Jet20 Internet (PA)', 'Jet20 (PI-22B)', 'Business Pro 500Mbps Bridge Mode ONT', 'BusinessPro150 (PI-22A)', 'Jet20 (PI-22I)', 'Jet20 (PI-22H)', 'Jet20 (PI-22F)', 'Hype75 Internet (PA)', 'Gamer-150 (bit)', 'Business 100 (WEJ)', 'Nova100 Via Alma', 'Business 100Mbps Via Alma', 'Sonic150 Combo (PA)', 'Nova100 Mbps Pakubuwono Menteng', 'Fast50 Internet (PA 12 Get 12)', 'Fantastic300 Mbps New', 'Demoline PoP 50 Mbps', 'Gamer150 Via Alma', 'Internet 750Mbps New', 'Pride 1 Gbps New', 'Prime500 Mbps New', 'Nova150 Mbps Pakubuwono Menteng', 'Hype75 Internet (AP77)', 'Fast50 Combo Internet A (AP77)', 'MyGamer250 Combo Internet A (AP77)', 'Nova100 Combo Internet A (AP77)', 'Hype75 Combo Internet A (AP77)', 'Supernova400 Mbps Pakubuwono', 'Ultra 1 Gbps Combo Internet A', 'Internet VIP NRO', 'Ultra 1Gbps Internet', 'VIP Rumah Ibadah', 'Fast50 Internet (PA 12 Get 6)', 'MyGamer250 Internet (PA 12 Get 6)', 'Nova 100 Internet (PA 12 Get 6)', 'Nova150 Combo Anandamaya New', 'Nova100 Combo Anandamaya', 'Fast50 Combo Anandamaya', 'Value30 Combo Internet A (PA 12 Get 12)', 'Jet20 Internet (PA3)', 'Nova100 Combo Internet A (PA 12 Get 12)', 'Fast50 Combo Internet A (PA 12 Get 12)', 'Jet20 Combo Internet A (PA)', 'Jet20 Internet (PA6)', 'Nova100 Internet (PA 12 Get 12)', 'Value30 Internet (PA3)', 'Value30 Internet (PA6)', 'MyGamer250 Combo Internet A (PA3)', 'Value30 Combo Internet A (PA6)', 'Nova 100 Internet (PA3)', 'Jet20 Combo Internet A (PA6)', 'Fast50 Internet (PA3)', 'MyGamer250 Internet (PA3)', 'Fast50 Internet (PA6)', 'Value30 Internet (PA 12 Get 6)', 'Value30 Combo Internet A (PA3)', 'Fast50 Combo Internet A (PA6)', 'Fast50 Combo Anandamaya NEW', 'Nova 100 Internet (PA6)', 'MyGamer250 Internet (PA6)')
                                 )
        
        tv_plan = st.selectbox('TV Plan',
                                  ('Tanpa Plan', 'StarTV', 'SmarTV+', 'Local Channel', 'STAR', 'Basic TV', 'Cosmic TV', 'Combo TV (Fast50)', 'SmarTV', 'No Channel', 'Combo TV (Hype75)', 'SMARTV', 'Combo TV (Nova100)', 'Combo TV (Value30)', 'Combo TV (Gamer150)', 'TV SOHO B (Movies and Sports)', 'Nova100 Mbps (ComboTV+ELKMS)', 'SMARTV+', 'Cosmic TV SOHO', 'Advance TV', 'TV SOHO A (News and lifestyle)', 'Star TV SOHO', 'Star TV Plus', 'StarTV Jet', 'Jet20 Mbps (ComboTV)', 'Combo TV (Jet20)', 'BASIC', 'Fast50 Mbps (ComboTV+ELKMS)', 'Xtra ComboTV (Fast50)', 'Hype75 Mbps (ComboTV+ELKMS)', 'Xtra ComboTV (Value30)', 'Xtra ComboTV (Gamer150)', 'Value30 Mbps (ComboTV+ELK)', 'Star TV Plus (Android)', 'Xtra ComboTV (Jet20)', 'Xtra ComboTV (Nova100)', 'Xtra ComboTV (Gamer75)', 'Xtra ComboTV (Fast50 + ELKMS)', 'Xtra ComboTV (V30 + ELK)', 'Xtra ComboTV Jet20 (Android)', 'Combo TV (Sonic150)', 'ComboTV Pakubuwono', 'ComboTV 77 Channel', 'Star TV', 'No Channel (0)', 'TV Only 60 Channel', 'TV Starter 15+', 'Local Channel (Android)', 'Advance TV (Android)', 'SOHO A', 'ComboTV Pakubuwono (Android)')
                                  )
        
        adv_promo = st.selectbox('Advance Promo', 
                                ('Tanpa Advance Promo', 'Kompensasi Diskon (Disc.50% x 3)', 'Promo Upsell 15% (Fast50 Mbps New) 6 bulan', 'RWB Promo Diskon 25% X 3', 'RWB Promo Diskon 50% X 6', 'Kompensasi Diskon (Disc.25% x 3)', 'RWB Promo Diskon 35%', 'Discount 30000 - PI21 (11Months)', 'Discount 15000 - PI21 (11months)', 'RWB Promo Diskon 35% X 6', 'Upsell Discount (20% 3 Months)', 'Promo Upsell 15% (Hype75 Mbps Combo New) 6 bulan', 'Promo Sinarmas Employee', 'Kompensasi Diskon (Disc.15% x 3)', 'Promo Upsell 15% (Fast50 Mbps Combo New) 6 bulan', 'Kompensasi Diskon (Disc.25% x 2)', 'Kompensasi Diskon (Disc.20% x 3)', 'Promo Upsell  Disc 15% (6 Bulan) Fast50', 'Promo Disc 20% (12 Bulan) Jet20 Mbps Combo New', 'RWB Promo Diskon 10% x 3 ', 'Promo Upsell 15% (Gamer150 New) 6 Bulan', 'Discount 10000 - PI21 (12Months)', 'Discount 30000 - PI21 (12Months)', 'Advance Payment Promo 9+3 (Existing)', 'Kompensasi Diskon (Disc.10% x 3)', 'RWB Promo Diskon 25% X 6', 'Discount 40000 - PI21 (11Months)', 'Promo Upsell 15% (Value30 Mbps Combo New) 6 bulan', 'RWB Promo Diskon 50% X 3', 'Promo Upsell Disc 15% (6 Bulan) Fast50 Combo A', 'Promo Upsell 15% (Hype75 Mbps New) 6 bulan', 'Promo Upsell Disc 15% (6 Bulan) Hype75 Combo A', 'Promo Upsell (Disc 15% 6 Bulan) MyGamer250 Mbps', 'Credit Card Payment Reward Discount (For Xtra)', 'Promo Upsell 15% (Value30 Mbps New) 6 bulan', 'Promo Upsell  Disc 15% (6 Bulan) Hype75', 'Credit Card Payment Reward Discount', 'Promo Upsell Disc 15% (6 Bulan) Value30 Combo A', 'Discount 15000 - PI21 (12months)', 'Advance Payment Promo 9+3 (New SA)', 'Promo Upsell  Disc 15% (6 Bulan) Nova100', 'New Year 2020 Promo (Bus 100 - 300)', 'New Year 2020 Promo (Bus 50)', 'New Year 2020 Promo (Bus Pro 150 - Pro 500)', 'Promo Ramadhan Up to 30% 2021 (Nova100 Mbps, Nova100 Combo, Sonic150 Combo)', 'Advance Payment Promo 9+3 (After SA)', 'Promo Ramadhan Up to 30% 2021 (Fast50 Mbps)', 'Promo Ramadhan Up to 30% 2021 (Fast50 Combo, Gamer150 Mbps, Gamer150 Combo)', 'Jet20 Mbps Special Discount 20%', 'Jet20 Mbps Special Discount 20% (6 Months)', 'Promo Dismantle 25% (Fast50 Mbps, Fast50 Combo, Business 50)', 'Promo Diskon Khusus Apartment Via Alma (100%)', 'Jet20 Mbps Special Discount 20% - Promo September 2021 (6 Months)', 'Nova100 Mbps Reg Discount 30% (for 6 Months)', 'Kompensasi Diskon (Disc.10% x 2)', '12 Month Advance Payment (Existing Customer)', 'Promo Sumpah Pemuda - 2021 (All Res)', 'Promo Hari Pahlawan - 2021 (All Res)', 'Promo Hari Pahlawan - 2021 (Sonic)', 'Promo Hari Pahlawan - 2021 (Gamer Combo)', 'Promo Akhir Tahun - 2021 (All Res)', 'Promo Akhir Tahun - 2021 (Gamer150 Mbps Reg)', 'Promo Akhir Tahun - 2021 (Nova100 Combo)', 'Promo Akhir Tahun - 2021 (All Business)', 'Promo New Area (Value30 Mbps New) 12 bulan', 'Promo Tahun Baru Disc 25% (6 Bulan)  Nova 100 Mbps Combo New', 'Promo Akhir Tahun - 2021 (Gamer Combo)', 'Promo New Area (Value30 Mbps Combo New) 12 bulan', 'Promo New Area (Hype75 Mbps New) 12 bulan', 'Promo Tahun Baru Disc 25% (6 Bulan) Nova 100 Mbps New ', 'Promo New Area (Fast50 Mbps New) 12 bulan', 'Promo New Area (Fast50 Mbps Combo New) 12 bulan', 'Promo New Area (Fast50 Mbps New) 6 bulan', 'Promo Tahun Baru Disc 25% (6 Bulan)  Gamer 150 Mbps New ', 'Promo New Area (Fast50 Mbps Combo New) 6 bulan', 'Promo Tahun Baru Disc 25% (6 Bulan)  Gamer 150 Mbps New', 'Promo New Area (Gamer150 New) 6 Bulan', 'Promo Tahun Baru Disc 25% (6 Bulan) Nova 100 Mbps New', 'Promo New Area (Value30 Mbps New) 6 bulan', ' Promo Special Thamrin Residence Disc 20% (6 Bulan) Fast50 Mbps New ', 'Promo New Area (Hype75 Mbps New) 6 bulan', 'Promo New Area (Value30 Mbps Combo New) 6 bulan', 'Promo Imlek Disc 15% (6 Bulan) Hype 75 Mbps New', 'Promo Imlek Disc 25% (6 Bulan)  Gamer 150 Mbps New', 'Promo Imlek Disc 25% (6 Bulan)  Nova 100 Mbps New ', 'Promo New Area (Nova100 New) 6 Bulan', 'Promo Special Thamrin Residence Disc 20% (6 Bulan) Hype75 Mbps New', 'Promo Special Thamrin Residence Disc 20% (6 Bulan) Gamer150 Combo New', 'Promo New Area Disc 20% (12 Bulan) Jet20 Mbps New', 'Promo Disc 20% (12 Bulan) Value30 Mbps New', 'Promo New Area Disc 20% (12 Bulan) Value30 Mbps New', 'Promo New Area Disc 20% (12 Bulan) Value30 Mbps Combo New', 'Promo New Area Disc 20% (12 Bulan) Fast50 Mbps New', 'Promo New Area Disc 20% (12 Bulan) Jet20 Mbps Combo New', 'Promo Disc 20% (12 Bulan) Fast50 Mbps Combo New', 'Promo New Area Disc 20% (12 Bulan) Nova100 Mbps Combo New', 'Promo New Area Disc 20% (12 Bulan) Hype75 Mbps New', 'Promo Disc 20% (12 Bulan) Jet20 Mbps New', 'Promo Imlek Disc 25% (6 Bulan)  Nova 100 Mbps Combo New ', 'Promo Disc 20% (12 Bulan) Fast50 Mbps New', 'Promo Disc 20% (12 Bulan) Value30 Mbps Combo New', 'Promo Disc 20% (12 Bulan) Business20 Mbps', 'Promo Disc 20% (12 Bulan) Gamer150 Mbps New', 'Promo Disc 20% (12 Bulan) Hype75 Mbps New', 'Promo Special Thamrin Residence Disc 20% (6 Bulan) Nova100 Mbps New ', 'Promo Nasional 2022 Disc 15% (6 Bulan) Nova100 Mbps New', 'Promo Disc 20% (12 Bulan) Nova100 Mbps New', 'Promo Nasional 2022 Disc 15% (6 Bulan) Nova100 Mbps Combo New', 'Promo Disc 20% (12 Bulan) Hype75 Mbps Combo New', 'Promo Thamrin Residence Disc 20% (6 Bulan) Fast50', 'Promo Nasional 2022 Disc 15% (6 Bulan) Gamer150 Mbps New', 'Promo Disc 20% (12 Bulan) Nova100 Mbps Combo New', 'Promo Nasional 2022 Disc 15% (6 Bulan) Gamer150 Mbps Combo New', 'Promo Ramadhan - Idul Fitri Disc 20% (12 Bulan) Fast50 Mbps Combo New', 'Promo Ramadhan - Idul Fitri Disc 20% (12 Bulan) Fast50 Mbps New', 'Promo Ramadhan - Idul Fitri Disc 20% (12 Bulan) Gamer150 Mbps New', 'Promo Ramadhan - Idul Fitri Disc 20% (12 Bulan) Hype75 Mbps New', 'Promo Disc 20% (12 Bulan) Business50 Mbps', 'Promo Ramadhan - Idul Fitri Disc 20% (12 Bulan) Gamer150 Mbps Combo New', 'Promo Ramadhan - Idul Fitri Disc 20% (12 Bulan) Nova100 Mbps New', 'Promo Ramadhan - Idul Fitri Disc 20% (12 Bulan) Nova100 Mbps Combo New', 'Promo Ramadhan - Idul Fitri Disc 20% (12 Bulan) Hype75 Mbps Combo New', 'Promo Ultah MyRep Disc 20% + 7% (12 Bulan) Fast50 Mbps New', 'Promo Ultah MyRep Disc 20% + 7% (12 Bulan) Hype75 Mbps New', 'Promo Ultah MyRep Disc 20% + 7% (12 Bulan) Gamer150 Mbps Combo New', 'Promo Ultah MyRep Disc 20% + 7% (12 Bulan) Gamer150 Mbps New', 'Promo Ultah MyRep Disc 20% + 7% (12 Bulan) Fast50 Mbps Combo New', 'Promo Ultah MyRep Disc 20% + 7% (12 Bulan) Nova100 Mbps New', 'Promo Ultah MyRep Disc 20% + 7% (12 Bulan) Hype75 Mbps Combo New', 'Promo Special Fast50 Mbps Disc 25% 12 Bulan', 'Promo Disc 20% (12 Bulan) Business100 Mbps', 'Promo Special Fast50 Combo Disc 25% 12 Bulan', 'Promo New Area (Gamer150 Combo New) 12 Bulan', 'Promo Disc 20% (12 Bulan) Business300 Mbps', 'Promo Disc 20% (12 Bulan) Value30 Combo A', 'Promo Disc 20% (12 Bulan) Jet20 Combo A', 'Promo Switching 2022 Disc 30% (12 Bulan) Jet20 Mbps Combo New', 'Promo Switching 2022 Disc 30% (12 Bulan) Jet20 Mbps New', 'Promo Switching 2022 Disc 30% (12 Bulan) Fast50 Mbps New', 'Promo Switching 2022 Disc 30% (12 Bulan) Hype75 Mbps New', 'Promo Switching 2022 Disc 30% (12 Bulan) Value30 Mbps New', 'Promo Switching 2022 Disc 30% (12 Bulan) Fast50 Mbps Combo New', 'Promo Switching 2022 Disc 30% (12 Bulan) Hype75 Mbps Combo New', 'Promo Switching 2022 Disc 30% (12 Bulan) Value30 Mbps Combo New', 'Promo Switching 2022 Disc 30% (12 Bulan) Nova100 Mbps Combo New', 'Promo Switching 2022 Disc 30% (12 Bulan) Gamer150 Mbps New', 'Promo New RFS Pekanbaru Disc 15% Jet20 Mbps New', 'Promo Disc 20% (12 Bulan) Business50 Mbps + TV', 'Promo Disc 20% (12 Bulan) Gamer150 Mbps Combo New', 'Promo New RFS Disc 15% Jet20 Mbps New', 'Promo Disc 20% (12 Bulan) Jet20', 'Promo New RFS Disc 15% Value30 Mbps New', 'Promo CLBK Disc 25% (12 Bulan) Value30 Mbps New', 'Promo CLBK Disc 25% (12 Bulan) Jet20 Mbps New', 'Promo New RFS Disc 25% Fast50 Mbps New', 'Promo New RFS Disc 25% Hype75 Mbps New', 'Promo New RFS Disc 15% Jet20 Mbps Combo New', 'Promo Disc 20% (12 Bulan) Fast50', 'Promo Disc 20% (12 Bulan) Value30', 'Promo New RFS Disc 25% Nova100 Mbps New', 'Promo Disc 20% (12 Bulan) Hype75', 'Promo CLBK Disc 25% (12 Bulan) Nova100 Mbps New', 'Promo Disc 15% (12 Bulan) Jet20', 'Promo Merdeka Disc 25% 6 Bulan (MyGamer250)', 'Promo Disc 20% (12 Bulan) Nova100', 'Promo Disc 20% 12 Bulan MyGamer250 Mbps', 'Promo Merdeka Disc 25% 6 Bulan (Nova100)', 'Promo Merdeka Disc 25% 6 Bulan (Nova100 Combo A)', 'Promo Disc 15% (12 Bulan) Value30', 'Promo CLBK Disc 25% (12 Bulan) Fast50 Internet', 'Promo CLBK Disc 25% (12 Bulan) Jet20 Combo A', 'Promo Disc 15% (12 Bulan) Jet20 Combo A', 'Promo Disc 20% (12 Bulan) Hype75 Combo A', 'Promo CLBK Disc 25% (12 Bulan) Jet20 Internet\t', 'Promo Disc 20% (12 Bulan) Nova100  Combo A', 'Promo Disc 20% (12 Bulan) Fast50 Combo A', 'Promo Nasional Disc 15% 6 Bulan (Nova100)', 'Promo Harbolnas September Value30 Internet', 'Promo Harbolnas September Fast50 Internet', 'Promo Harbolnas September Value30 Combo A', 'Promo Nasional (Disc 15% 6 Bulan) MyGamer250 Mbps', 'Promo Harbolnas September Nova100 Internet', 'Promo Harbolnas September Fast50 Combo A', 'Promo Harbolnas September MyGamer250 Internet', 'Promo Nasional Disc 15% 6 Bulan (Nova100 Combo A)', 'Promo Disc 15% (12 Bulan) Fast50', 'Promo New RFS HRB Disc 20% (6 Bulan) Fast50', 'Promo Disc 25% (12 Bulan) Fast50 Combo A', 'Promo Oktober 2022 Disc 25% (12 Bulan) Fast50 Internet', 'Promo Oktober 2022 Disc 25% (12 Bulan) Nova100 Internet', 'Promo Shocktober Disc 25% (12 Bulan) Jet20', 'Promo Shocktober Disc 30% (12 Bulan) Nova100 Combo A', 'Promo Shocktober Disc 25% (12 Bulan) Value30 Combo A', 'Promo Shocktober Disc 25% (12 Bulan) Value30 Internet', 'Promo Shocktober Disc 30% (12 Bulan) Fast50 Internet', 'Promo Disc 20% (12 Bulan) BusinessPro500 Mbps', 'Promo WOW FLASH SALE Value30 Internet', 'Promo WOW FLASH SALE Value30 Combo A', 'Promo WOW-VEMBER DEALS Value30 Internet', 'Promo WOW-VEMBER DEALS Fast50 Combo A', 'Promo WOW-VEMBER DEALS Fast50 Internet', 'Promo WOW-VEMBER DEALS Value30 Combo A', 'Promo MyRep YES Value30 Internet', 'Kompensasi Diskon (Disc.50% x 2)', 'Kompensasi Diskon (Disc.15% x 2)', 'Promo Upsell (Disc 15% 6 Bulan) MyGamer250 Combo A', 'Promo Upsell 15% (Gamer150 Combo New) 6 Bulan', 'Promo Upsell Disc 15% (6 Bulan) Nova100 Combo A', 'Promo Upsell 15% (Nova100 New) 6 Bulan', 'Promo New Area (Nova100 Combo New) 12 Bulan', 'Promo Upsell  Disc 15% (6 Bulan) Value30', '3 Month Advance Payment', 'Discount 40000 - PI21 (12Months)', 'Discount 35000 - PI21 (12Months)', 'Kompensasi Diskon (Disc.50% x 1)', 'Kompensasi Diskon (Disc.10% x 1)', 'Kompensasi Diskon (Disc.15% x 1)', 'Kompensasi Diskon (Disc.20% x 1)', 'Kompensasi Diskon (Disc.25% x 1)', 'Discount VIP NRO 2021 (12months)', 'Promo New Area (Nova100 New) 12 Bulan', '12 Month Advance Payment (New SA)', 'Advance Payment 6 Month', 'Promo Tahun Baru Disc 25% (6 Bulan)  Gamer 150 Mbps Combo New', 'Promo New Area Disc 20% (12 Bulan) Gamer150 Mbps New', 'Promo New Area Disc 20% (12 Bulan) Nova100 Mbps New', 'Promo New Area Disc 20% (12 Bulan) Gamer150 Mbps Combo New', 'Promo New Area Disc 20% (12 Bulan) Fast50 Mbps Combo New', 'Promo New Area Disc 20% (12 Bulan) Business20 Mbps + TV', 'Promo New Area Disc 20% (12 Bulan) Business20 Mbps', 'Promo Disc 20% (12 Bulan) Business20 Mbps + TV', 'Discount VIP NRO 2021 (24months)', 'Promo Ultah MyRep Disc 20% + 7% (12 Bulan) Nova100 Mbps Combo New', 'Promo Disc 20% (12 Bulan) BusinessPro150 Mbps', 'Discount VIP NRO 2021 (36months)', 'Disc Demoline PoP 50 Mbps', 'Promo Switching 2022 Disc 30% (12 Bulan) Nova100 Mbps New', 'Promo Switching 2022 Disc 30% (12 Bulan) Gamer150 Mbps Combo New', 'Promo New RFS Pekanbaru Disc 15% Jet20 Mbps Combo New', 'Promo CLBK Disc 25% (12 Bulan) Value30 Mbps Combo New', '3 Months Advance Payment for selected vendor', 'Promo New RFS Disc 15% Value30 Mbps Combo New', 'Promo CLBK Disc 25% (12 Bulan) Fast50 Mbps New', 'Promo CLBK Disc 25% (12 Bulan) Jet20 Mbps Combo New', 'Promo CLBK Disc 25% (12 Bulan) Nova100 Mbps Combo New', 'Promo CLBK Disc 25% (12 Bulan) Hype75 Mbps New', 'Promo CLBK Disc 25% (12 Bulan) Business20 Mbps', 'Promo New RFS Disc 25% Gamer150 Mbps New ', 'Promo New RFS Disc 25% Fast50 Mbps Combo New', 'Promo Disc 20% (12 Bulan) Business300 Mbps + TV', 'Promo CLBK Disc 25% (12 Bulan) Gamer150 Mbps New', 'Discount VIP NRO 2021 (6months)', 'Promo Thamrin Residence Disc 20% (6 Bulan) Fast50 Combo A', 'Promo Thamrin Residence Disc 20% (6 Bulan) Nova100 ', 'Promo Disc 25% (12 Bulan) Fast50', 'Promo Disc20% 12 Bulan MyGamer250 Combo A', 'Promo Disc 25% (12 Bulan) Nova100', 'Promo Disc 25% (12 Bulan) Nova100  Combo A', 'Promo New RFS Lampung dan Pekanbaru  (Disc 25% 12 Bulan)  MyGamer250 Combo A', 'Promo Disc 25% (12 Bulan) Hype75', 'Promo Thamrin Residence MyGamer250 Mbps', 'Promo Disc 15% (12 Bulan) Value30 Combo A', 'Promo New RFS Lampung dan Pekanbaru  (Disc 25% 12 Bulan)  MyGamer250 Mbps', 'Promo Merdeka Disc 25% 6 Bulan (MyGamer250 Combo A)', 'Promo Disc 25% (12 Bulan) Business300 Mbps', 'Promo CLBK Disc 25% (12 Bulan) Value30 Internet', 'Promo CLBK Disc 25% (12 Bulan) Value30 Combo A', 'Promo CLBK Disc 25% (12 Bulan) Business50 Mbps', 'Promo Disc 25% (12 Bulan) Business50 Mbps', 'Promo CLBK Disc 25% (12 Bulan) Hype75 Internet', 'Promo Nasional (Disc 15% 6 Bulan) MyGamer250 Combo A', 'Promo Thamrin Residence Disc 20% (6 Bulan) Hype75', 'Promo Thamrin Residence MyGamer250 Combo A', 'Promo Thamrin Residence Disc 20% (6 Bulan) Hype75 Combo A', 'Promo CLBK Disc 25% (12 Bulan) MyGamer250 Internet', 'Promo CLBK Disc 25% (12 Bulan) Nova100 Internet', 'Promo New RFS HRB Disc 20% (6 Bulan) Nova100 ', ' Promo Flash Sale 9.9 Value30 Internet ', 'Promo Harbolnas September MyGamer250 Combo A', 'Promo Harbolnas September Nova100 Combo A', 'Promo New RFS HRB MyGamer250 Mbps', 'Promo Oktober 2022 Disc 25% (12 Bulan) Nova100 Combo A', 'Promo New RFS HRB Disc 20% (6 Bulan) Fast50 Combo A', 'Promo CLBK Disc 25% (12 Bulan) MyGamer250 Combo A', 'Discount VIP NRO (12months)', 'Promo Oktober 2022 Disc 25% (12 Bulan) MyGamer250 Internet', 'Promo Disc 25% (12 Bulan) Business100 Mbps', 'Discount VIP NRO (24months)', 'Discount VIP NRO (6months)', 'Promo CLBK Disc 25% (12 Bulan) Fast50 Combo A', 'Promo Disc 15% (12 Bulan) MyGamer250', 'Promo Disc 20% (12 Bulan) Business100 Mbps + TV', 'Discount VIP NRO (36months)', 'Promo Internet VIP Rumah Ibadah', 'Promo Oktober 2022 Disc 25% (12 Bulan) Fast50 Combo A', 'Promo Oktober 2022 Disc 25% (12 Bulan) MyGamer250 Combo A', 'Promo Ruko Special Price Disc 15% (6 Bulan) Jet20 Internet', 'Promo Ruko Special Price Disc 15% (6 Bulan) Jet20 Combo A', 'Promo Ruko Special Price Disc 15% (6 Bulan) Value30 Internet', 'Promo Ruko Special Price Disc 15% (6 Bulan) FiberPro20', 'Promo CLBK Disc 25% (12 Bulan) Nova100 Combo A', 'Promo Ruko Special Price Disc 15% (6 Bulan) MyGamer250 Internet', 'Promo Ruko Special Price Disc 15% (6 Bulan) Fast50 Internet', 'Promo Disc 15% (12 Bulan) Business20 Mbps', 'Promo Shocktober Disc 25% (12 Bulan) Jet20 Combo A', 'Promo Shocktober Disc 30% (12 Bulan) Nova100 Internet', 'Promo Shocktober Disc 30% (12 Bulan) MyGamer250 Internet', 'Promo Shocktober Disc 30% (12 Bulan) Fast50 Combo A', 'Promo Shocktober Disc 30% (12 Bulan) MyGamer250 Combo A', 'Promo Ruko Special Price Disc 15% (6 Bulan) Nova100 Internet', 'Promo Disc 25% (12 Bulan) Value30 Combo A', 'Promo WOW-VEMBER DEALS Nova100 Internet', 'Promo Disc 25% (12 Bulan) Value30', 'Promo MyRep YES Value30 Combo A', 'Promo New RFS HRB Disc 15% (6 Bulan) Nova100 Combo A', 'Discount VIP NRO (3months)', 'Promo New RFS HRB Disc 20% (6 Bulan) Nova100 Combo A', 'Promo WOW FLASH SALE MyGamer250 Internet', 'Promo WOW FLASH SALE Fast50 Internet', 'Promo WOW FLASH SALE Nova100 Internet', 'Promo WOW FLASH SALE Fast50 Combo A', 'Promo WOW FLASH SALE Nova100 Combo A', 'Promo WOW FLASH SALE MyGamer250 Combo A', 'Promo WOW-VEMBER DEALS MyGamer250 Internet', 'Promo WOW-VEMBER DEALS Nova100 Combo A', 'Promo WOW-VEMBER DEALS MyGamer250 Combo A', 'Promo Ruko Special Price Disc 15% (6 Bulan) FiberPro60', 'Promo Akhir Tahun 2022 Disc 20% (12 Bulan) Nova100', 'Promo MyRep YES Fast50 Internet', 'Promo Disc 25% (12 Bulan) Business300 Mbps + TV', 'Promo New RFS HRB Disc 15% (6 Bulan) Nova100 Internet', 'Promo New RFS HRB Disc 20% (6 Bulan) MyGamer250 Mbps', 'Promo Akhir Tahun 2022 Disc 20% (12 Bulan) Fast50', 'Promo Akhir Tahun 2022 Disc 20% (12 Bulan) Fast50 Combo A', 'Promo Akhir Tahun 2022 Disc 20% (12 Bulan) MyGamer250', 'Promo Akhir Tahun 2022 Disc 20% (12 Bulan) MyGamer250 Combo A', 'Promo HRB YES Disc 30% Fast50 Internet (3 Bulan)', 'Promo HRB YES Disc 30% Value30 Internet (3 Bulan)', 'Promo Disc 20% (12 Bulan) Advance Payment', 'Promo MyRep YES Nova100 Internet', 'Promo MyRep YES Fast50 Combo A', 'Promo MyRep YES Nova100 Combo A', 'Promo Disc 15% (12 Bulan) Advance Payment', 'Promo MyRep YES MyGamer250 Internet', 'Promo MyRep YES MyGamer250 Combo A', 'Promo New Year New Value Internet', 'Promo Disc 22%+12% (12 Bulan) Advance Payment', 'Promo Akhir Tahun 2022 Disc 20% (12 Bulan) Nova100  Combo A', 'Promo Nasional 2023 Disc. 15% (12 Bulan) Jet20', 'Promo New RFS HRB Disc 15% (6 Bulan) MyGamer250 Internet', 'Promo HRB YES Disc 30% MyGamer250 Combo A', 'Promo HRB YES Disc 30% Nova100 Internet (3 Bulan)', 'Promo HRB YES Disc 30% MyGamer250 Internet (3 Bulan)', 'Promo HRB YES Disc 30% Fast50 Combo A', 'Promo HRB YES Disc 30% Value30 Combo A', 'Flash Sale Puri Casablanca Disc 50% (6 Bulan) MyGamer250 Internet', 'Promo Disc 25% (12 Bulan) BusinessPro150 Mbps', 'Promo New Year New Value Combo', 'Promo Nasional 2023 Disc. 15% (12 Bulan) Value30', 'Promo Disc 30% (12 Bulan) MyGamer250', 'Promo Nasional 2023 Disc. 25% (12 Bulan) Nova100 Combo A', 'Promo Nasional 2023 Disc. 20% (12 Bulan) Fast50', 'Promo Nasional 2023 Disc. 15% (12 Bulan) Jet20 Combo A', 'Promo Nasional 2023 Disc. 15% (12 Bulan) Value30 Combo A', 'Promo Nasional 2023 Disc. 25% (12 Bulan) MyGamer250', 'Promo Nasional 2023 Disc. 25% (12 Bulan) Nova100', 'Promo New Year New Value (Advance Payment)', 'Promo Nasional 2023 Disc. 25% (12 Bulan) MyGamer250 Combo A', 'Promo Nasional 2023 Disc. 20% (12 Bulan) Fast50 Combo A', 'Promo Nasional 2023 (PA 5 Get 1) Fast50 Combo Internet A', 'Promo Nasional 2023 (PA 5 Get 1) Fast50', 'Promo New RFS HRB Disc 15% (6 Bulan) Value30 Internet', 'Promo Nasional 2023 (PA 5 Get 1) Jet20', 'Promo Nasional 2023 (PA 5 Get 1) Value30', 'Promo Disc 30% (12 Bulan) Nova100', 'Promo Nasional 2023 (PA 5 Get 1) Nova100', 'Promo Nasional 2023 (PA 5 Get 1) Value30 Combo Internet A', 'Promo Nasional 2023 (PA 5 Get 1) MyGamer250')
                                )
        
        comp_cs = st.slider('Complaint by Customer Service', min_value = 0.0, max_value = 200.0 ,step=1.0)
        comp_email = st.slider('Complaint by Email', min_value = 0.0, max_value = 250.0 ,step=1.0)
        comp_socmed = st.slider('Complaint by Social Media', min_value = 0.0, max_value = 200.0 ,step=1.0)
        comp_tel = st.slider('Complaint by Telegram', min_value = 0.0, max_value = 100.0 ,step=1.0)
        comp_wa = st.slider('Complaint by Whatsapp', min_value = 0.0, max_value = 400.0 ,step=1.0)
        comp_wic = st.slider('Complaint by WIC', min_value = 0.0, max_value = 150.0 ,step=1.0)
        output=""
        output1=""
        
        user_df_data = [[user_area,user_plan,tv_plan,adv_promo,comp_cs,comp_email,comp_socmed,comp_tel,comp_wa,comp_wic]]
        user_df_colnames = ["Area Name","Plan","Tv Plan","Advance Promo","Complaint by Customer Service","Complaint by Email","Complaint by Social Media","Complaint by Telegram","Complaint by Whatsapp","Complaint by WIC"]

        input_df = pd.DataFrame(user_df_data,columns = user_df_colnames)
        
        if st.button("Predict"):
            result_df = predict_churn(input_df)
            if result_df.iloc[0]['Churn'] == 0:
                st.success(f' The customer will be Not Churn')
            else:
                st.success(f'The customer will be Churn')

    elif add_selectbox == 'Batch':
        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])
        if file_upload is not None:
            try:
                data = pd.read_csv(file_upload)

                # Mengecek apakah semua kolom yang diharapkan ada di DataFrame
                if not set(expected_columns).issubset(data.columns):
                    raise ValueError('Terdapat satu / beberapa kolom yang dibutuhkan, tidak ada pada file upload!')

                # visualize_df = 
                result_df = predict_churn(data)
                visualize_data_batch(data)
            except ValueError as ve:
                st.error(f'Error: {ve}')
            except Exception as e:
                st.error(f'Unexpected error occurred: {e}')

            # data = pd.read_csv(file_upload)
            # result_df = predict_churn(data)
            # visualize_data_batch(data)

    elif add_selectbox == 'About':
        st.subheader("Customer Churn Prediction & Reporting")
        st.subheader("Taufiq Ahmadi")
        st.subheader("https://www.linkedin.com/in/amd-taufiq/")
        st.button("Re-run")

if __name__ == '__main__':
    # setup(data=pd.DataFrame(input_df), target='Churn')
    run()