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
import numpy as np

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

area_dict = {'Bali': 0, 'Bandung': 1, 'Bekasi': 2, 'Bogor': 3, 'Cibubur': 4, 'Cilegon': 5, 'Cirebon': 6, 'Depok': 7, 'Jakarta': 8, 'Jambi': 9, 'Karawang': 10, 'Lampung': 11, 'Makassar': 12, 'Malang': 13, 'Medan': 14, 'Palembang': 15, 'Pekanbaru': 16, 'Purwokerto': 17, 'Semarang': 18, 'Serang': 19, 'Solo': 20, 'Surabaya': 21, 'Tangerang': 22, 'Tegal': 23}

plan_dict = {'AMAZING (50 Mbps + TV SD & HD Channels)': 0, 'Alpha 10 Mbps': 1, 'BASIC SUPER (Internet Up To 512 Kbps + TV Channel)': 2, 'BLITZ (Internet Up To 20 Mbps)': 3, 'BSD Basic 10 Mbps': 4, 'BSD Pro 300 Mbps': 5, 'BSD Smash (300 Mbps + TV)': 6, 'BSD Value (100 Mbps + TV)': 7, 'Basic (promo tv booster)': 8, 'Basic 30 Mbps': 9, 'Basic Plus Cosmic': 10, 'Basic Plus Star': 11, 'Basic.15+': 12, 'Basic.8+': 13, 'Basic15': 14, 'Basic15+': 15, 'Basic30+': 16, 'Basic8': 17, 'Bright': 18, 'Business 10 Mbps': 19, 'Business 10 Mbps (free installation fee)': 20, 'Business 100 (PI20)': 21, 'Business 100 (PI21)': 22, 'Business 100 (WEJ)': 23, 'Business 100 Mbps': 24, 'Business 100 Mbps (Promo Buy 1 Get 1)': 25, 'Business 100 Mbps (free installation fee)': 26, 'Business 100Mbps Via Alma': 27, 'Business 20 (PI20)': 28, 'Business 20 (PI21)': 29, 'Business 20 Mbps': 30, 'Business 30 Mbps': 31, 'Business 30 Mbps (free installation fee)': 32, 'Business 300 (PI20)': 33, 'Business 300 (PI21)': 34, 'Business 300 Mbps': 35, 'Business 300 Mbps (Promo Buy 1 Get 1)': 36, 'Business 300 Mbps (free installation fee)': 37, 'Business 50 (PI20)': 38, 'Business 50 (PI21)': 39, 'Business 50 Mbps': 40, 'Business 75 (PI20)': 41, 'Business Pro 100 Mbps': 42, 'Business Pro 150  (PI20)': 43, 'Business Pro 150 (PI21)': 44, 'Business Pro 150 Mbps': 45, 'Business Pro 500 (PI20)': 46, 'Business Pro 500 (PI21)': 47, 'Business Pro 500 Mbps': 48, 'Business Pro 500Mbps Bridge Mode ONT': 49, 'Business.300 Mbps Reg': 50, 'Business.50 Mbps Reg': 51, 'Business100 (PI-22A)': 52, 'Business100 (PI-22B)': 53, 'Business100 Mbps (PA)': 54, 'Business20 (PI-22A)': 55, 'Business20 (PI-22B)': 56, 'Business20 Mbps (PA)': 57, 'Business300 (PI-22A)': 58, 'Business300 (PI-22B)': 59, 'Business300 (PI-22C)': 60, 'Business300 Mbps (PA)': 61, 'Business50 (PI-22A)': 62, 'Business50 (PI-22B)': 63, 'Business50 (PI-22C)': 64, 'Business50 Mbps (PA)': 65, 'BusinessPro 150 Mbps (PA)': 66, 'BusinessPro 500 Mbps (PA)': 67, 'BusinessPro.150 Mbps Reg': 68, 'BusinessPro150 (PI-22A)': 69, 'BusinessPro150 (PI-22B)': 70, 'BusinessPro150 (PI-22C)': 71, 'BusinessPro150 (PI-22D)': 72, 'Demoline PoP 50 Mbps': 73, 'EazyNet (Bonus TV)': 74, 'FESTIVE (40 Mbps + TV SD & HD Channels)': 75, 'FUN (10 Mbps + TV SD & HD Channels)': 76, 'FUN Promo': 77, 'Fantastic300 Mbps New': 78, 'Fast 50 Mbps': 79, 'Fast 50 Mbps+': 80, 'Fast 50 Mbps+ HITS': 81, 'Fast 50 Mbps+ XTRA': 82, 'Fast-50': 83, 'Fast-50 (bit)': 84, 'Fast-50 (fs)': 85, 'Fast-50 (smt)': 86, 'Fast-50 Super93 (1x)': 87, 'Fast-50 Super93 (2x)': 88, 'Fast.50': 89, 'Fast50 (PI-22A)': 90, 'Fast50 (PI-22B)': 91, 'Fast50 (PI-22C)': 92, 'Fast50 (PI-22D)': 93, 'Fast50 (PI-22E)': 94, 'Fast50 (PI-22F)': 95, 'Fast50 (PI-22G)': 96, 'Fast50 (PI-22H)': 97, 'Fast50 (PI-22I)': 98, 'Fast50 (PI-22J)': 99, 'Fast50 (PI-22K)': 100, 'Fast50 (PI-22L)': 101, 'Fast50 (PI20-A)': 102, 'Fast50 (PI20-B)': 103, 'Fast50 (PI21-A)': 104, 'Fast50 (PI21-B)': 105, 'Fast50 (PI21-C)': 106, 'Fast50 (PI21-D)': 107, 'Fast50 (PI21-E)': 108, 'Fast50 Combo': 109, 'Fast50 Combo (PA)': 110, 'Fast50 Combo (PI-22A)': 111, 'Fast50 Combo (PI-22B)': 112, 'Fast50 Combo (PI-22C)': 113, 'Fast50 Combo Anandamaya': 114, 'Fast50 Combo Anandamaya NEW': 115, 'Fast50 Combo Internet A': 116, 'Fast50 Combo Internet A (AP77)': 117, 'Fast50 Combo Internet A (PA 12 Get 12)': 118, 'Fast50 Combo Internet A (PA 12 Get 6)': 119, 'Fast50 Combo Internet A (PA)': 120, 'Fast50 Combo Internet A (PA6)': 121, 'Fast50 Combo New': 122, 'Fast50 Combo New (PA)': 123, 'Fast50 Internet': 124, 'Fast50 Internet (AP77)': 125, 'Fast50 Internet (PA 12 Get 12)': 126, 'Fast50 Internet (PA 12 Get 6)': 127, 'Fast50 Internet (PA)': 128, 'Fast50 Internet (PA3)': 129, 'Fast50 Internet (PA6)': 130, 'Fast50 Mbps': 131, 'Fast50 Mbps (PA)': 132, 'Fast50 Mbps New': 133, 'Fast50 Mbps New (PA)': 134, 'Fast50 Mbps+ Xtra ComboTV': 135, 'Fast50 Special': 136, 'Fast50 Special 2': 137, 'Fast50 Via Alma': 138, 'Fast50+': 139, 'FiberPro 120': 140, 'FiberPro 120 (PI-21)': 141, 'FiberPro 20': 142, 'FiberPro 20 (PI-21)': 143, 'FiberPro 300': 144, 'FiberPro 300 (PI-21)': 145, 'FiberPro 60': 146, 'FiberPro 60 (PI-21)': 147, 'Flash75 ComboTV Pakubuwono': 148, 'GAMER.150+': 149, 'GAMER150+': 150, 'GAMERX50+': 151, 'Gamer (promo tv booster)': 152, 'Gamer 150 Mbps+': 153, 'Gamer 150 Mbps+ XTRA': 154, 'Gamer 150 Mbps+ Xtra ComboTV': 155, 'Gamer 75 Mbps+': 156, 'Gamer 75 Mbps+ XTRA': 157, 'Gamer 75 Mbps+ Xtra ComboTV': 158, 'Gamer-150': 159, 'Gamer-150 (bit)': 160, 'Gamer-150 (fs)': 161, 'Gamer-150 (smt)': 162, 'Gamer-150 Super93 (1x)': 163, 'Gamer-150 Super93 (2x)': 164, 'Gamer150 (PI-22A)': 165, 'Gamer150 (PI-22B)': 166, 'Gamer150 (PI-22C)': 167, 'Gamer150 (PI-22D)': 168, 'Gamer150 (PI20-A)': 169, 'Gamer150 (PI20-B)': 170, 'Gamer150 (PI21-A)': 171, 'Gamer150 (PI21-B)': 172, 'Gamer150 (PI21-C)': 173, 'Gamer150 (PI21-D)': 174, 'Gamer150 Combo': 175, 'Gamer150 Combo (PA)': 176, 'Gamer150 Combo New': 177, 'Gamer150 Combo New (PA)': 178, 'Gamer150 ComboTV Pakubuwono': 179, 'Gamer150 Mbps': 180, 'Gamer150 Mbps New': 181, 'Gamer150 Mbps New (PA)': 182, 'Gamer150 Mbps Reg': 183, 'Gamer150 Mbps Reg (PA)': 184, 'Gamer150 Via Alma': 185, 'Gamer150+ XTRA (PI-22A)': 186, 'Gamer200 Mbps Pakubuwono': 187, 'Gamer50': 188, 'Gamer50 (PI-22A)': 189, 'Gamer50 (PI-22B)': 190, 'Gamer50 (PI-22C)': 191, 'Gamer50 (PI20-A)': 192, 'Gamer50 (PI21-A)': 193, 'GamerX.50+': 194, 'GamerX50': 195, 'Hype75 (PI-22A)': 196, 'Hype75 Combo Internet A': 197, 'Hype75 Combo Internet A (AP77)': 198, 'Hype75 Combo Internet A (PA)': 199, 'Hype75 Combo New': 200, 'Hype75 Combo New (PA)': 201, 'Hype75 Internet': 202, 'Hype75 Internet (AP77)': 203, 'Hype75 Internet (PA)': 204, 'Hype75 Mbps New': 205, 'Hype75 Mbps New (PA)': 206, 'IBS.CA Business 50 Mbps': 207, 'IBS.CA Business 50 Mbps (PI-21)': 208, 'IBS.CA Business Pro 150 Mbps': 209, 'IBS.CA Business100': 210, 'IBS.CA Business100 (PI-21)': 211, 'IBS.CA Business20': 212, 'IBS.CA Business30': 213, 'IBS.CA Business30 (PI-21)': 214, 'IBS.CA Business300': 215, 'IBS.CA Business300 (PI-21)': 216, 'IBS.CA Roket100': 217, 'IBS.CA Roket100 (PI-21)': 218, 'IBS.CA-Fiber120+': 219, 'IBS.CA-Fiber120+ (PI-21)': 220, 'IBS.CA-Fiber60+': 221, 'IBS.CA-Fiber60+ (PI-21)': 222, 'Internet 750Mbps New': 223, 'Internet Up To 3 Mbps': 224, 'Internet Up To 512 Kbps': 225, 'Internet VIP NRO': 226, 'Jet 20 Mbps+': 227, 'Jet 20 Mbps+ HITS': 228, 'Jet 20 PLUS': 229, 'Jet 20 PLUS AP12': 230, 'Jet 20 PLUS AP6': 231, 'Jet-20': 232, 'Jet-20 - winback': 233, 'Jet20': 234, 'Jet20 (PI-22A)': 235, 'Jet20 (PI-22B)': 236, 'Jet20 (PI-22C)': 237, 'Jet20 (PI-22D)': 238, 'Jet20 (PI-22E)': 239, 'Jet20 (PI-22F)': 240, 'Jet20 (PI-22G)': 241, 'Jet20 (PI-22H)': 242, 'Jet20 (PI-22I)': 243, 'Jet20 (PI-22K)': 244, 'Jet20 (PI20-A)': 245, 'Jet20 (PI20-B)': 246, 'Jet20 (PI21-A)': 247, 'Jet20 (PI21-B)': 248, 'Jet20 (PI21-C)': 249, 'Jet20 (PI21-D)': 250, 'Jet20 Combo': 251, 'Jet20 Combo (PA)': 252, 'Jet20 Combo (PI-22A)': 253, 'Jet20 Combo Internet A': 254, 'Jet20 Combo Internet A (PA3)': 255, 'Jet20 Combo Internet A (PA6)': 256, 'Jet20 Combo New': 257, 'Jet20 Internet': 258, 'Jet20 Internet (PA)': 259, 'Jet20 Internet (PA3)': 260, 'Jet20 Internet (PA6)': 261, 'Jet20 Lite': 262, 'Jet20 Mbps': 263, 'Jet20 Mbps (PA)': 264, 'Jet20 Mbps New': 265, 'Jet20 Mbps+ Xtra ComboTV': 266, 'Lite (Package Internet Up To 3 Mbps & TV)': 267, 'Magic Wifi 200': 268, 'Magic Wifi 200 (PI21)': 269, 'MyGamer250 Combo Internet A': 270, 'MyGamer250 Combo Internet A (AP77)': 271, 'MyGamer250 Combo Internet A (PA 12 Get 12)': 272, 'MyGamer250 Combo Internet A (PA 12 Get 6)': 273, 'MyGamer250 Combo Internet A (PA)': 274, 'MyGamer250 Combo Internet A (PA3)': 275, 'MyGamer250 Internet (AP77)': 276, 'MyGamer250 Internet (PA 12 Get 12)': 277, 'MyGamer250 Internet (PA 12 Get 6)': 278, 'MyGamer250 Internet (PA3)': 279, 'MyGamer250 Internet (PA6)': 280, 'MyGamer250 Mbps': 281, 'MyGamer250 Mbps Internet (PA)': 282, 'Nova (promo tv booster)': 283, 'Nova 100 Internet (AP77)': 284, 'Nova 100 Internet (PA 12 Get 6)': 285, 'Nova 100 Internet (PA)': 286, 'Nova 100 Internet (PA3)': 287, 'Nova 100 Internet (PA6)': 288, 'Nova 100 Mbps+': 289, 'Nova 100 Mbps+ HITS': 290, 'Nova 100 Mbps+ XTRA': 291, 'Nova 100 Mbps+ Xtra ComboTV': 292, 'Nova Package': 293, 'Nova Plus Cosmic': 294, 'Nova Plus Star': 295, 'Nova Plus Star (diskon 25% 12 bulan)': 296, 'Nova-100': 297, 'Nova-100 (bit)': 298, 'Nova-100 (fs)': 299, 'Nova-100 (smt)': 300, 'Nova-100 Super93 (1x)': 301, 'Nova-100 Super93 (2x)': 302, 'Nova.100+': 303, 'Nova100 (PI-22A)': 304, 'Nova100 (PI-22B)': 305, 'Nova100 (PI-22C)': 306, 'Nova100 (PI-22D)': 307, 'Nova100 (PI-22E)': 308, 'Nova100 (PI-22F)': 309, 'Nova100 (PI-22G)': 310, 'Nova100 (PI-22H)': 311, 'Nova100 (PI-22I)': 312, 'Nova100 (PI-22J)': 313, 'Nova100 (PI-22L)': 314, 'Nova100 (PI-22M)': 315, 'Nova100 (PI20-A)': 316, 'Nova100 (PI20-B)': 317, 'Nova100 (PI21-A)': 318, 'Nova100 (PI21-B)': 319, 'Nova100 (PI21-C)': 320, 'Nova100 (PI21-D)': 321, 'Nova100 Combo': 322, 'Nova100 Combo (PA)': 323, 'Nova100 Combo (PI-22A)': 324, 'Nova100 Combo (PI-22B)': 325, 'Nova100 Combo Anandamaya': 326, 'Nova100 Combo Internet A': 327, 'Nova100 Combo Internet A (AP77)': 328, 'Nova100 Combo Internet A (PA 12 Get 12)': 329, 'Nova100 Combo Internet A (PA)': 330, 'Nova100 Combo New': 331, 'Nova100 Combo New (PA)': 332, 'Nova100 Internet': 333, 'Nova100 Internet (PA 12 Get 12)': 334, 'Nova100 Mbps': 335, 'Nova100 Mbps Lite': 336, 'Nova100 Mbps Lite (PA)': 337, 'Nova100 Mbps New': 338, 'Nova100 Mbps New (PA)': 339, 'Nova100 Mbps Pakubuwono': 340, 'Nova100 Mbps Pakubuwono Menteng': 341, 'Nova100 Mbps Reg': 342, 'Nova100 Mbps Reg (PA)': 343, 'Nova100 Special': 344, 'Nova100 Via Alma': 345, 'Nova100+': 346, 'Nova150 (PI-22A)': 347, 'Nova150 (PI-22B)': 348, 'Nova150 (PI21-A)': 349, 'Nova150 (PI21-B)': 350, 'Nova150 Combo Anandamaya New': 351, 'Nova150 Mbps Pakubuwono Menteng': 352, 'Nova150 Special': 353, 'Nova150 Special 2': 354, 'Package Internet Up To 10 Mbps & TV Starter 15+': 355, 'Pride 1 Gbps New': 356, 'Prime500 Mbps New': 357, 'Rapid': 358, 'Retain 10Mbps': 359, 'Retain 10Mbps AdvanceTV': 360, 'SNAP (Internet Up To 10 Mbps)': 361, 'SUPER (20 Mbps + TV SD & HD Channels) KOWIS LEWIS': 362, 'SUPER Promo': 363, 'Snap Plus (Bonus TV)': 364, 'Sonic150 Combo': 365, 'Sonic150 Combo (PA)': 366, 'Starter 6 Mbps': 367, 'SuperNova Package': 368, 'SuperNova-300': 369, 'SuperNova-300 (fs)': 370, 'SuperNova300 (PI-21)': 371, 'SuperNova300+': 372, 'Supernova300 ComboTV Pakubuwono': 373, 'Supernova300 Mbps (PA)': 374, 'Supernova400 Mbps Pakubuwono': 375, 'Tanpa Plan': 376, 'Ultra 1 Gbps Combo Internet A': 377, 'Ultra 1Gbps Internet': 378, 'VALUE PROMO': 379, 'VALUE SUPER (Internet Up To 1 Mbps + TV Channel)': 380, 'VIP NRO 2021': 381, 'VIP NRO 2021 (FS)': 382, 'VIP NRO 2021+': 383, 'VIP Rumah Ibadah': 384, 'Value 30 Mbps+': 385, 'Value 30 Mbps+ HITS': 386, 'Value 30 Mbps+ XTRA': 387, 'Value-30': 388, 'Value-30 (bit)': 389, 'Value-30 (fs)': 390, 'Value-30 (smt)': 391, 'Value-30 Super93 (1x)': 392, 'Value-30 Super93 (2x)': 393, 'Value30': 394, 'Value30 (PI-22A)': 395, 'Value30 (PI-22B)': 396, 'Value30 (PI-22C)': 397, 'Value30 (PI-22D)': 398, 'Value30 (PI-22E)': 399, 'Value30 (PI-22F)': 400, 'Value30 (PI-22G)': 401, 'Value30 (PI-22H)': 402, 'Value30 (PI-22I)': 403, 'Value30 (PI-22J)': 404, 'Value30 (PI-22K)': 405, 'Value30 (PI-22M)': 406, 'Value30 (PI-22N)': 407, 'Value30 (PI20-A)': 408, 'Value30 (PI20-B)': 409, 'Value30 (PI21-A)': 410, 'Value30 (PI21-B)': 411, 'Value30 (PI21-C)': 412, 'Value30 (PI21-D)': 413, 'Value30 (PI21-E)': 414, 'Value30 Combo': 415, 'Value30 Combo (PA)': 416, 'Value30 Combo (PI-22A)': 417, 'Value30 Combo (PI-22B)': 418, 'Value30 Combo Internet A': 419, 'Value30 Combo Internet A (AP77)': 420, 'Value30 Combo Internet A (PA 12 Get 12)': 421, 'Value30 Combo Internet A (PA)': 422, 'Value30 Combo Internet A (PA3)': 423, 'Value30 Combo Internet A (PA6)': 424, 'Value30 Combo New': 425, 'Value30 Combo New (PA)': 426, 'Value30 Internet': 427, 'Value30 Internet (AP77)': 428, 'Value30 Internet (PA 12 Get 12)': 429, 'Value30 Internet (PA 12 Get 6)': 430, 'Value30 Internet (PA)': 431, 'Value30 Internet (PA3)': 432, 'Value30 Internet (PA6)': 433, 'Value30 Mbps': 434, 'Value30 Mbps (PA)': 435, 'Value30 Mbps New': 436, 'Value30 Mbps+ Xtra ComboTV': 437, 'Value30 New (PA)': 438, 'Value30 Special': 439, 'Value30 Special 2': 440, 'XTREME (100 Mbps + TV SD & HD Channels)': 441}


dict_tvplan = {'Advance TV': 0, 'Advance TV (Android)': 1, 'BASIC': 2, 'Basic TV': 3, 'Combo TV (Fast50)': 4, 'Combo TV (Gamer150)': 5, 'Combo TV (Hype75)': 6, 'Combo TV (Jet20)': 7, 'Combo TV (Nova100)': 8, 'Combo TV (Sonic150)': 9, 'Combo TV (Value30)': 10, 'ComboTV 77 Channel': 11, 'ComboTV Pakubuwono': 12, 'ComboTV Pakubuwono (Android)': 13, 'Cosmic TV': 14, 'Cosmic TV SOHO': 15, 'Fast50 Mbps (ComboTV+ELKMS)': 16, 'Hype75 Mbps (ComboTV+ELKMS)': 17, 'Jet20 Mbps (ComboTV)': 18, 'Local Channel': 19, 'Local Channel (Android)': 20, 'No Channel': 21, 'No Channel (0)': 22, 'Nova100 Mbps (ComboTV+ELKMS)': 23, 'SMARTV': 24, 'SMARTV+': 25, 'SOHO A': 26, 'STAR': 27, 'SmarTV': 28, 'SmarTV+': 29, 'Star TV': 30, 'Star TV Plus': 31, 'Star TV Plus (Android)': 32, 'Star TV SOHO': 33, 'StarTV': 34, 'StarTV Jet': 35, 'TV Only 60 Channel': 36, 'TV SOHO A (News and lifestyle)': 37, 'TV SOHO B (Movies and Sports)': 38, 'TV Starter 15+': 39, 'Tanpa Plan': 40, 'Value30 Mbps (ComboTV+ELK)': 41, 'Xtra ComboTV (Fast50 + ELKMS)': 42, 'Xtra ComboTV (Fast50)': 43, 'Xtra ComboTV (Gamer150)': 44, 'Xtra ComboTV (Gamer75)': 45, 'Xtra ComboTV (Jet20)': 46, 'Xtra ComboTV (Nova100)': 47, 'Xtra ComboTV (V30 + ELK)': 48, 'Xtra ComboTV (Value30)': 49, 'Xtra ComboTV Jet20 (Android)': 50}


dict_promo = {' Promo Flash Sale 9.9 Value30 Internet ': 0, ' Promo Special Thamrin Residence Disc 20% (6 Bulan) Fast50 Mbps New ': 1, '12 Month Advance Payment (Existing Customer)': 2, '12 Month Advance Payment (New SA)': 3, '3 Month Advance Payment': 4, '3 Months Advance Payment for selected vendor': 5, 'Advance Payment 6 Month': 6, 'Advance Payment Promo 9+3 (After SA)': 7, 'Advance Payment Promo 9+3 (Existing)': 8, 'Advance Payment Promo 9+3 (New SA)': 9, 'Credit Card Payment Reward Discount': 10, 'Credit Card Payment Reward Discount (For Xtra)': 11, 'Disc Demoline PoP 50 Mbps': 12, 'Discount 10000 - PI21 (12Months)': 13, 'Discount 15000 - PI21 (11months)': 14, 'Discount 15000 - PI21 (12months)': 15, 'Discount 30000 - PI21 (11Months)': 16, 'Discount 30000 - PI21 (12Months)': 17, 'Discount 35000 - PI21 (12Months)': 18, 'Discount 40000 - PI21 (11Months)': 19, 'Discount 40000 - PI21 (12Months)': 20, 'Discount VIP NRO (12months)': 21, 'Discount VIP NRO (24months)': 22, 'Discount VIP NRO (36months)': 23, 'Discount VIP NRO (3months)': 24, 'Discount VIP NRO (6months)': 25, 'Discount VIP NRO 2021 (12months)': 26, 'Discount VIP NRO 2021 (24months)': 27, 'Discount VIP NRO 2021 (36months)': 28, 'Discount VIP NRO 2021 (6months)': 29, 'Flash Sale Puri Casablanca Disc 50% (6 Bulan) MyGamer250 Internet': 30, 'Jet20 Mbps Special Discount 20%': 31, 'Jet20 Mbps Special Discount 20% (6 Months)': 32, 'Jet20 Mbps Special Discount 20% - Promo September 2021 (6 Months)': 33, 'Kompensasi Diskon (Disc.10% x 1)': 34, 'Kompensasi Diskon (Disc.10% x 2)': 35, 'Kompensasi Diskon (Disc.10% x 3)': 36, 'Kompensasi Diskon (Disc.15% x 1)': 37, 'Kompensasi Diskon (Disc.15% x 2)': 38, 'Kompensasi Diskon (Disc.15% x 3)': 39, 'Kompensasi Diskon (Disc.20% x 1)': 40, 'Kompensasi Diskon (Disc.20% x 3)': 41, 'Kompensasi Diskon (Disc.25% x 1)': 42, 'Kompensasi Diskon (Disc.25% x 2)': 43, 'Kompensasi Diskon (Disc.25% x 3)': 44, 'Kompensasi Diskon (Disc.50% x 1)': 45, 'Kompensasi Diskon (Disc.50% x 2)': 46, 'Kompensasi Diskon (Disc.50% x 3)': 47, 'New Year 2020 Promo (Bus 100 - 300)': 48, 'New Year 2020 Promo (Bus 50)': 49, 'New Year 2020 Promo (Bus Pro 150 - Pro 500)': 50, 'Nova100 Mbps Reg Discount 30% (for 6 Months)': 51, 'Promo Akhir Tahun - 2021 (All Business)': 52, 'Promo Akhir Tahun - 2021 (All Res)': 53, 'Promo Akhir Tahun - 2021 (Gamer Combo)': 54, 'Promo Akhir Tahun - 2021 (Gamer150 Mbps Reg)': 55, 'Promo Akhir Tahun - 2021 (Nova100 Combo)': 56, 'Promo Akhir Tahun 2022 Disc 20% (12 Bulan) Fast50': 57, 'Promo Akhir Tahun 2022 Disc 20% (12 Bulan) Fast50 Combo A': 58, 'Promo Akhir Tahun 2022 Disc 20% (12 Bulan) MyGamer250': 59, 'Promo Akhir Tahun 2022 Disc 20% (12 Bulan) MyGamer250 Combo A': 60, 'Promo Akhir Tahun 2022 Disc 20% (12 Bulan) Nova100': 61, 'Promo Akhir Tahun 2022 Disc 20% (12 Bulan) Nova100  Combo A': 62, 'Promo CLBK Disc 25% (12 Bulan) Business20 Mbps': 63, 'Promo CLBK Disc 25% (12 Bulan) Business50 Mbps': 64, 'Promo CLBK Disc 25% (12 Bulan) Fast50 Combo A': 65, 'Promo CLBK Disc 25% (12 Bulan) Fast50 Internet': 66, 'Promo CLBK Disc 25% (12 Bulan) Fast50 Mbps New': 67, 'Promo CLBK Disc 25% (12 Bulan) Gamer150 Mbps New': 68, 'Promo CLBK Disc 25% (12 Bulan) Hype75 Internet': 69, 'Promo CLBK Disc 25% (12 Bulan) Hype75 Mbps New': 70, 'Promo CLBK Disc 25% (12 Bulan) Jet20 Combo A': 71, 'Promo CLBK Disc 25% (12 Bulan) Jet20 Internet\t': 72, 'Promo CLBK Disc 25% (12 Bulan) Jet20 Mbps Combo New': 73, 'Promo CLBK Disc 25% (12 Bulan) Jet20 Mbps New': 74, 'Promo CLBK Disc 25% (12 Bulan) MyGamer250 Combo A': 75, 'Promo CLBK Disc 25% (12 Bulan) MyGamer250 Internet': 76, 'Promo CLBK Disc 25% (12 Bulan) Nova100 Combo A': 77, 'Promo CLBK Disc 25% (12 Bulan) Nova100 Internet': 78, 'Promo CLBK Disc 25% (12 Bulan) Nova100 Mbps Combo New': 79, 'Promo CLBK Disc 25% (12 Bulan) Nova100 Mbps New': 80, 'Promo CLBK Disc 25% (12 Bulan) Value30 Combo A': 81, 'Promo CLBK Disc 25% (12 Bulan) Value30 Internet': 82, 'Promo CLBK Disc 25% (12 Bulan) Value30 Mbps Combo New': 83, 'Promo CLBK Disc 25% (12 Bulan) Value30 Mbps New': 84, 'Promo Disc 15% (12 Bulan) Advance Payment': 85, 'Promo Disc 15% (12 Bulan) Business20 Mbps': 86, 'Promo Disc 15% (12 Bulan) Fast50': 87, 'Promo Disc 15% (12 Bulan) Jet20': 88, 'Promo Disc 15% (12 Bulan) Jet20 Combo A': 89, 'Promo Disc 15% (12 Bulan) MyGamer250': 90, 'Promo Disc 15% (12 Bulan) Value30': 91, 'Promo Disc 15% (12 Bulan) Value30 Combo A': 92, 'Promo Disc 20% (12 Bulan) Advance Payment': 93, 'Promo Disc 20% (12 Bulan) Business100 Mbps': 94, 'Promo Disc 20% (12 Bulan) Business100 Mbps + TV': 95, 'Promo Disc 20% (12 Bulan) Business20 Mbps': 96, 'Promo Disc 20% (12 Bulan) Business20 Mbps + TV': 97, 'Promo Disc 20% (12 Bulan) Business300 Mbps': 98, 'Promo Disc 20% (12 Bulan) Business300 Mbps + TV': 99, 'Promo Disc 20% (12 Bulan) Business50 Mbps': 100, 'Promo Disc 20% (12 Bulan) Business50 Mbps + TV': 101, 'Promo Disc 20% (12 Bulan) BusinessPro150 Mbps': 102, 'Promo Disc 20% (12 Bulan) BusinessPro500 Mbps': 103, 'Promo Disc 20% (12 Bulan) Fast50': 104, 'Promo Disc 20% (12 Bulan) Fast50 Combo A': 105, 'Promo Disc 20% (12 Bulan) Fast50 Mbps Combo New': 106, 'Promo Disc 20% (12 Bulan) Fast50 Mbps New': 107, 'Promo Disc 20% (12 Bulan) Gamer150 Mbps Combo New': 108, 'Promo Disc 20% (12 Bulan) Gamer150 Mbps New': 109, 'Promo Disc 20% (12 Bulan) Hype75': 110, 'Promo Disc 20% (12 Bulan) Hype75 Combo A': 111, 'Promo Disc 20% (12 Bulan) Hype75 Mbps Combo New': 112, 'Promo Disc 20% (12 Bulan) Hype75 Mbps New': 113, 'Promo Disc 20% (12 Bulan) Jet20': 114, 'Promo Disc 20% (12 Bulan) Jet20 Combo A': 115, 'Promo Disc 20% (12 Bulan) Jet20 Mbps Combo New': 116, 'Promo Disc 20% (12 Bulan) Jet20 Mbps New': 117, 'Promo Disc 20% (12 Bulan) Nova100': 118, 'Promo Disc 20% (12 Bulan) Nova100  Combo A': 119, 'Promo Disc 20% (12 Bulan) Nova100 Mbps Combo New': 120, 'Promo Disc 20% (12 Bulan) Nova100 Mbps New': 121, 'Promo Disc 20% (12 Bulan) Value30': 122, 'Promo Disc 20% (12 Bulan) Value30 Combo A': 123, 'Promo Disc 20% (12 Bulan) Value30 Mbps Combo New': 124, 'Promo Disc 20% (12 Bulan) Value30 Mbps New': 125, 'Promo Disc 20% 12 Bulan MyGamer250 Mbps': 126, 'Promo Disc 22%+12% (12 Bulan) Advance Payment': 127, 'Promo Disc 25% (12 Bulan) Business100 Mbps': 128, 'Promo Disc 25% (12 Bulan) Business300 Mbps': 129, 'Promo Disc 25% (12 Bulan) Business300 Mbps + TV': 130, 'Promo Disc 25% (12 Bulan) Business50 Mbps': 131, 'Promo Disc 25% (12 Bulan) BusinessPro150 Mbps': 132, 'Promo Disc 25% (12 Bulan) Fast50': 133, 'Promo Disc 25% (12 Bulan) Fast50 Combo A': 134, 'Promo Disc 25% (12 Bulan) Hype75': 135, 'Promo Disc 25% (12 Bulan) Nova100': 136, 'Promo Disc 25% (12 Bulan) Nova100  Combo A': 137, 'Promo Disc 25% (12 Bulan) Value30': 138, 'Promo Disc 25% (12 Bulan) Value30 Combo A': 139, 'Promo Disc 30% (12 Bulan) MyGamer250': 140, 'Promo Disc 30% (12 Bulan) Nova100': 141, 'Promo Disc20% 12 Bulan MyGamer250 Combo A': 142, 'Promo Diskon Khusus Apartment Via Alma (100%)': 143, 'Promo Dismantle 25% (Fast50 Mbps, Fast50 Combo, Business 50)': 144, 'Promo HRB YES Disc 30% Fast50 Combo A': 145, 'Promo HRB YES Disc 30% Fast50 Internet (3 Bulan)': 146, 'Promo HRB YES Disc 30% MyGamer250 Combo A': 147, 'Promo HRB YES Disc 30% MyGamer250 Internet (3 Bulan)': 148, 'Promo HRB YES Disc 30% Nova100 Internet (3 Bulan)': 149, 'Promo HRB YES Disc 30% Value30 Combo A': 150, 'Promo HRB YES Disc 30% Value30 Internet (3 Bulan)': 151, 'Promo Harbolnas September Fast50 Combo A': 152, 'Promo Harbolnas September Fast50 Internet': 153, 'Promo Harbolnas September MyGamer250 Combo A': 154, 'Promo Harbolnas September MyGamer250 Internet': 155, 'Promo Harbolnas September Nova100 Combo A': 156, 'Promo Harbolnas September Nova100 Internet': 157, 'Promo Harbolnas September Value30 Combo A': 158, 'Promo Harbolnas September Value30 Internet': 159, 'Promo Hari Pahlawan - 2021 (All Res)': 160, 'Promo Hari Pahlawan - 2021 (Gamer Combo)': 161, 'Promo Hari Pahlawan - 2021 (Sonic)': 162, 'Promo Imlek Disc 15% (6 Bulan) Hype 75 Mbps New': 163, 'Promo Imlek Disc 25% (6 Bulan)  Gamer 150 Mbps New': 164, 'Promo Imlek Disc 25% (6 Bulan)  Nova 100 Mbps Combo New ': 165, 'Promo Imlek Disc 25% (6 Bulan)  Nova 100 Mbps New ': 166, 'Promo Internet VIP Rumah Ibadah': 167, 'Promo Merdeka Disc 25% 6 Bulan (MyGamer250 Combo A)': 168, 'Promo Merdeka Disc 25% 6 Bulan (MyGamer250)': 169, 'Promo Merdeka Disc 25% 6 Bulan (Nova100 Combo A)': 170, 'Promo Merdeka Disc 25% 6 Bulan (Nova100)': 171, 'Promo MyRep YES Fast50 Combo A': 172, 'Promo MyRep YES Fast50 Internet': 173, 'Promo MyRep YES MyGamer250 Combo A': 174, 'Promo MyRep YES MyGamer250 Internet': 175, 'Promo MyRep YES Nova100 Combo A': 176, 'Promo MyRep YES Nova100 Internet': 177, 'Promo MyRep YES Value30 Combo A': 178, 'Promo MyRep YES Value30 Internet': 179, 'Promo Nasional (Disc 15% 6 Bulan) MyGamer250 Combo A': 180, 'Promo Nasional (Disc 15% 6 Bulan) MyGamer250 Mbps': 181, 'Promo Nasional 2022 Disc 15% (6 Bulan) Gamer150 Mbps Combo New': 182, 'Promo Nasional 2022 Disc 15% (6 Bulan) Gamer150 Mbps New': 183, 'Promo Nasional 2022 Disc 15% (6 Bulan) Nova100 Mbps Combo New': 184, 'Promo Nasional 2022 Disc 15% (6 Bulan) Nova100 Mbps New': 185, 'Promo Nasional 2023 (PA 5 Get 1) Fast50': 186, 'Promo Nasional 2023 (PA 5 Get 1) Fast50 Combo Internet A': 187, 'Promo Nasional 2023 (PA 5 Get 1) Jet20': 188, 'Promo Nasional 2023 (PA 5 Get 1) MyGamer250': 189, 'Promo Nasional 2023 (PA 5 Get 1) Nova100': 190, 'Promo Nasional 2023 (PA 5 Get 1) Value30': 191, 'Promo Nasional 2023 (PA 5 Get 1) Value30 Combo Internet A': 192, 'Promo Nasional 2023 Disc. 15% (12 Bulan) Jet20': 193, 'Promo Nasional 2023 Disc. 15% (12 Bulan) Jet20 Combo A': 194, 'Promo Nasional 2023 Disc. 15% (12 Bulan) Value30': 195, 'Promo Nasional 2023 Disc. 15% (12 Bulan) Value30 Combo A': 196, 'Promo Nasional 2023 Disc. 20% (12 Bulan) Fast50': 197, 'Promo Nasional 2023 Disc. 20% (12 Bulan) Fast50 Combo A': 198, 'Promo Nasional 2023 Disc. 25% (12 Bulan) MyGamer250': 199, 'Promo Nasional 2023 Disc. 25% (12 Bulan) MyGamer250 Combo A': 200, 'Promo Nasional 2023 Disc. 25% (12 Bulan) Nova100': 201, 'Promo Nasional 2023 Disc. 25% (12 Bulan) Nova100 Combo A': 202, 'Promo Nasional Disc 15% 6 Bulan (Nova100 Combo A)': 203, 'Promo Nasional Disc 15% 6 Bulan (Nova100)': 204, 'Promo New Area (Fast50 Mbps Combo New) 12 bulan': 205, 'Promo New Area (Fast50 Mbps Combo New) 6 bulan': 206, 'Promo New Area (Fast50 Mbps New) 12 bulan': 207, 'Promo New Area (Fast50 Mbps New) 6 bulan': 208, 'Promo New Area (Gamer150 Combo New) 12 Bulan': 209, 'Promo New Area (Gamer150 New) 6 Bulan': 210, 'Promo New Area (Hype75 Mbps New) 12 bulan': 211, 'Promo New Area (Hype75 Mbps New) 6 bulan': 212, 'Promo New Area (Nova100 Combo New) 12 Bulan': 213, 'Promo New Area (Nova100 New) 12 Bulan': 214, 'Promo New Area (Nova100 New) 6 Bulan': 215, 'Promo New Area (Value30 Mbps Combo New) 12 bulan': 216, 'Promo New Area (Value30 Mbps Combo New) 6 bulan': 217, 'Promo New Area (Value30 Mbps New) 12 bulan': 218, 'Promo New Area (Value30 Mbps New) 6 bulan': 219, 'Promo New Area Disc 20% (12 Bulan) Business20 Mbps': 220, 'Promo New Area Disc 20% (12 Bulan) Business20 Mbps + TV': 221, 'Promo New Area Disc 20% (12 Bulan) Fast50 Mbps Combo New': 222, 'Promo New Area Disc 20% (12 Bulan) Fast50 Mbps New': 223, 'Promo New Area Disc 20% (12 Bulan) Gamer150 Mbps Combo New': 224, 'Promo New Area Disc 20% (12 Bulan) Gamer150 Mbps New': 225, 'Promo New Area Disc 20% (12 Bulan) Hype75 Mbps New': 226, 'Promo New Area Disc 20% (12 Bulan) Jet20 Mbps Combo New': 227, 'Promo New Area Disc 20% (12 Bulan) Jet20 Mbps New': 228, 'Promo New Area Disc 20% (12 Bulan) Nova100 Mbps Combo New': 229, 'Promo New Area Disc 20% (12 Bulan) Nova100 Mbps New': 230, 'Promo New Area Disc 20% (12 Bulan) Value30 Mbps Combo New': 231, 'Promo New Area Disc 20% (12 Bulan) Value30 Mbps New': 232, 'Promo New RFS Disc 15% Jet20 Mbps Combo New': 233, 'Promo New RFS Disc 15% Jet20 Mbps New': 234, 'Promo New RFS Disc 15% Value30 Mbps Combo New': 235, 'Promo New RFS Disc 15% Value30 Mbps New': 236, 'Promo New RFS Disc 25% Fast50 Mbps Combo New': 237, 'Promo New RFS Disc 25% Fast50 Mbps New': 238, 'Promo New RFS Disc 25% Gamer150 Mbps New ': 239, 'Promo New RFS Disc 25% Hype75 Mbps New': 240, 'Promo New RFS Disc 25% Nova100 Mbps New': 241, 'Promo New RFS HRB Disc 15% (6 Bulan) MyGamer250 Internet': 242, 'Promo New RFS HRB Disc 15% (6 Bulan) Nova100 Combo A': 243, 'Promo New RFS HRB Disc 15% (6 Bulan) Nova100 Internet': 244, 'Promo New RFS HRB Disc 15% (6 Bulan) Value30 Internet': 245, 'Promo New RFS HRB Disc 20% (6 Bulan) Fast50': 246, 'Promo New RFS HRB Disc 20% (6 Bulan) Fast50 Combo A': 247, 'Promo New RFS HRB Disc 20% (6 Bulan) MyGamer250 Mbps': 248, 'Promo New RFS HRB Disc 20% (6 Bulan) Nova100 ': 249, 'Promo New RFS HRB Disc 20% (6 Bulan) Nova100 Combo A': 250, 'Promo New RFS HRB MyGamer250 Mbps': 251, 'Promo New RFS Lampung dan Pekanbaru  (Disc 25% 12 Bulan)  MyGamer250 Combo A': 252, 'Promo New RFS Lampung dan Pekanbaru  (Disc 25% 12 Bulan)  MyGamer250 Mbps': 253, 'Promo New RFS Pekanbaru Disc 15% Jet20 Mbps Combo New': 254, 'Promo New RFS Pekanbaru Disc 15% Jet20 Mbps New': 255, 'Promo New Year New Value (Advance Payment)': 256, 'Promo New Year New Value Combo': 257, 'Promo New Year New Value Internet': 258, 'Promo Oktober 2022 Disc 25% (12 Bulan) Fast50 Combo A': 259, 'Promo Oktober 2022 Disc 25% (12 Bulan) Fast50 Internet': 260, 'Promo Oktober 2022 Disc 25% (12 Bulan) MyGamer250 Combo A': 261, 'Promo Oktober 2022 Disc 25% (12 Bulan) MyGamer250 Internet': 262, 'Promo Oktober 2022 Disc 25% (12 Bulan) Nova100 Combo A': 263, 'Promo Oktober 2022 Disc 25% (12 Bulan) Nova100 Internet': 264, 'Promo Ramadhan - Idul Fitri Disc 20% (12 Bulan) Fast50 Mbps Combo New': 265, 'Promo Ramadhan - Idul Fitri Disc 20% (12 Bulan) Fast50 Mbps New': 266, 'Promo Ramadhan - Idul Fitri Disc 20% (12 Bulan) Gamer150 Mbps Combo New': 267, 'Promo Ramadhan - Idul Fitri Disc 20% (12 Bulan) Gamer150 Mbps New': 268, 'Promo Ramadhan - Idul Fitri Disc 20% (12 Bulan) Hype75 Mbps Combo New': 269, 'Promo Ramadhan - Idul Fitri Disc 20% (12 Bulan) Hype75 Mbps New': 270, 'Promo Ramadhan - Idul Fitri Disc 20% (12 Bulan) Nova100 Mbps Combo New': 271, 'Promo Ramadhan - Idul Fitri Disc 20% (12 Bulan) Nova100 Mbps New': 272, 'Promo Ramadhan Up to 30% 2021 (Fast50 Combo, Gamer150 Mbps, Gamer150 Combo)': 273, 'Promo Ramadhan Up to 30% 2021 (Fast50 Mbps)': 274, 'Promo Ramadhan Up to 30% 2021 (Nova100 Mbps, Nova100 Combo, Sonic150 Combo)': 275, 'Promo Ruko Special Price Disc 15% (6 Bulan) Fast50 Internet': 276, 'Promo Ruko Special Price Disc 15% (6 Bulan) FiberPro20': 277, 'Promo Ruko Special Price Disc 15% (6 Bulan) FiberPro60': 278, 'Promo Ruko Special Price Disc 15% (6 Bulan) Jet20 Combo A': 279, 'Promo Ruko Special Price Disc 15% (6 Bulan) Jet20 Internet': 280, 'Promo Ruko Special Price Disc 15% (6 Bulan) MyGamer250 Internet': 281, 'Promo Ruko Special Price Disc 15% (6 Bulan) Nova100 Internet': 282, 'Promo Ruko Special Price Disc 15% (6 Bulan) Value30 Internet': 283, 'Promo Shocktober Disc 25% (12 Bulan) Jet20': 284, 'Promo Shocktober Disc 25% (12 Bulan) Jet20 Combo A': 285, 'Promo Shocktober Disc 25% (12 Bulan) Value30 Combo A': 286, 'Promo Shocktober Disc 25% (12 Bulan) Value30 Internet': 287, 'Promo Shocktober Disc 30% (12 Bulan) Fast50 Combo A': 288, 'Promo Shocktober Disc 30% (12 Bulan) Fast50 Internet': 289, 'Promo Shocktober Disc 30% (12 Bulan) MyGamer250 Combo A': 290, 'Promo Shocktober Disc 30% (12 Bulan) MyGamer250 Internet': 291, 'Promo Shocktober Disc 30% (12 Bulan) Nova100 Combo A': 292, 'Promo Shocktober Disc 30% (12 Bulan) Nova100 Internet': 293, 'Promo Sinarmas Employee': 294, 'Promo Special Fast50 Combo Disc 25% 12 Bulan': 295, 'Promo Special Fast50 Mbps Disc 25% 12 Bulan': 296, 'Promo Special Thamrin Residence Disc 20% (6 Bulan) Gamer150 Combo New': 297, 'Promo Special Thamrin Residence Disc 20% (6 Bulan) Hype75 Mbps New': 298, 'Promo Special Thamrin Residence Disc 20% (6 Bulan) Nova100 Mbps New ': 299, 'Promo Sumpah Pemuda - 2021 (All Res)': 300, 'Promo Switching 2022 Disc 30% (12 Bulan) Fast50 Mbps Combo New': 301, 'Promo Switching 2022 Disc 30% (12 Bulan) Fast50 Mbps New': 302, 'Promo Switching 2022 Disc 30% (12 Bulan) Gamer150 Mbps Combo New': 303, 'Promo Switching 2022 Disc 30% (12 Bulan) Gamer150 Mbps New': 304, 'Promo Switching 2022 Disc 30% (12 Bulan) Hype75 Mbps Combo New': 305, 'Promo Switching 2022 Disc 30% (12 Bulan) Hype75 Mbps New': 306, 'Promo Switching 2022 Disc 30% (12 Bulan) Jet20 Mbps Combo New': 307, 'Promo Switching 2022 Disc 30% (12 Bulan) Jet20 Mbps New': 308, 'Promo Switching 2022 Disc 30% (12 Bulan) Nova100 Mbps Combo New': 309, 'Promo Switching 2022 Disc 30% (12 Bulan) Nova100 Mbps New': 310, 'Promo Switching 2022 Disc 30% (12 Bulan) Value30 Mbps Combo New': 311, 'Promo Switching 2022 Disc 30% (12 Bulan) Value30 Mbps New': 312, 'Promo Tahun Baru Disc 25% (6 Bulan)  Gamer 150 Mbps Combo New': 313, 'Promo Tahun Baru Disc 25% (6 Bulan)  Gamer 150 Mbps New': 314, 'Promo Tahun Baru Disc 25% (6 Bulan)  Gamer 150 Mbps New ': 315, 'Promo Tahun Baru Disc 25% (6 Bulan)  Nova 100 Mbps Combo New': 316, 'Promo Tahun Baru Disc 25% (6 Bulan) Nova 100 Mbps New': 317, 'Promo Tahun Baru Disc 25% (6 Bulan) Nova 100 Mbps New ': 318, 'Promo Thamrin Residence Disc 20% (6 Bulan) Fast50': 319, 'Promo Thamrin Residence Disc 20% (6 Bulan) Fast50 Combo A': 320, 'Promo Thamrin Residence Disc 20% (6 Bulan) Hype75': 321, 'Promo Thamrin Residence Disc 20% (6 Bulan) Hype75 Combo A': 322, 'Promo Thamrin Residence Disc 20% (6 Bulan) Nova100 ': 323, 'Promo Thamrin Residence MyGamer250 Combo A': 324, 'Promo Thamrin Residence MyGamer250 Mbps': 325, 'Promo Ultah MyRep Disc 20% + 7% (12 Bulan) Fast50 Mbps Combo New': 326, 'Promo Ultah MyRep Disc 20% + 7% (12 Bulan) Fast50 Mbps New': 327, 'Promo Ultah MyRep Disc 20% + 7% (12 Bulan) Gamer150 Mbps Combo New': 328, 'Promo Ultah MyRep Disc 20% + 7% (12 Bulan) Gamer150 Mbps New': 329, 'Promo Ultah MyRep Disc 20% + 7% (12 Bulan) Hype75 Mbps Combo New': 330, 'Promo Ultah MyRep Disc 20% + 7% (12 Bulan) Hype75 Mbps New': 331, 'Promo Ultah MyRep Disc 20% + 7% (12 Bulan) Nova100 Mbps Combo New': 332, 'Promo Ultah MyRep Disc 20% + 7% (12 Bulan) Nova100 Mbps New': 333, 'Promo Upsell  Disc 15% (6 Bulan) Fast50': 334, 'Promo Upsell  Disc 15% (6 Bulan) Hype75': 335, 'Promo Upsell  Disc 15% (6 Bulan) Nova100': 336, 'Promo Upsell  Disc 15% (6 Bulan) Value30': 337, 'Promo Upsell (Disc 15% 6 Bulan) MyGamer250 Combo A': 338, 'Promo Upsell (Disc 15% 6 Bulan) MyGamer250 Mbps': 339, 'Promo Upsell 15% (Fast50 Mbps Combo New) 6 bulan': 340, 'Promo Upsell 15% (Fast50 Mbps New) 6 bulan': 341, 'Promo Upsell 15% (Gamer150 Combo New) 6 Bulan': 342, 'Promo Upsell 15% (Gamer150 New) 6 Bulan': 343, 'Promo Upsell 15% (Hype75 Mbps Combo New) 6 bulan': 344, 'Promo Upsell 15% (Hype75 Mbps New) 6 bulan': 345, 'Promo Upsell 15% (Nova100 New) 6 Bulan': 346, 'Promo Upsell 15% (Value30 Mbps Combo New) 6 bulan': 347, 'Promo Upsell 15% (Value30 Mbps New) 6 bulan': 348, 'Promo Upsell Disc 15% (6 Bulan) Fast50 Combo A': 349, 'Promo Upsell Disc 15% (6 Bulan) Hype75 Combo A': 350, 'Promo Upsell Disc 15% (6 Bulan) Nova100 Combo A': 351, 'Promo Upsell Disc 15% (6 Bulan) Value30 Combo A': 352, 'Promo WOW FLASH SALE Fast50 Combo A': 353, 'Promo WOW FLASH SALE Fast50 Internet': 354, 'Promo WOW FLASH SALE MyGamer250 Combo A': 355, 'Promo WOW FLASH SALE MyGamer250 Internet': 356, 'Promo WOW FLASH SALE Nova100 Combo A': 357, 'Promo WOW FLASH SALE Nova100 Internet': 358, 'Promo WOW FLASH SALE Value30 Combo A': 359, 'Promo WOW FLASH SALE Value30 Internet': 360, 'Promo WOW-VEMBER DEALS Fast50 Combo A': 361, 'Promo WOW-VEMBER DEALS Fast50 Internet': 362, 'Promo WOW-VEMBER DEALS MyGamer250 Combo A': 363, 'Promo WOW-VEMBER DEALS MyGamer250 Internet': 364, 'Promo WOW-VEMBER DEALS Nova100 Combo A': 365, 'Promo WOW-VEMBER DEALS Nova100 Internet': 366, 'Promo WOW-VEMBER DEALS Value30 Combo A': 367, 'Promo WOW-VEMBER DEALS Value30 Internet': 368, 'RWB Promo Diskon 10% x 3 ': 369, 'RWB Promo Diskon 25% X 3': 370, 'RWB Promo Diskon 25% X 6': 371, 'RWB Promo Diskon 35%': 372, 'RWB Promo Diskon 35% X 6': 373, 'RWB Promo Diskon 50% X 3': 374, 'RWB Promo Diskon 50% X 6': 375, 'Tanpa Advance Promo': 376, 'Upsell Discount (20% 3 Months)': 377}

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
    reverse_data = reverse(data)
    return data, reverse_data

def load_churned(data):
    data = data[data['Churn'] == 'Churn']
    # Area Name
    unique_values_area_churned = data['Area Name'].unique()
    count_area_churned = data['Area Name'].value_counts()[unique_values_area_churned]
    area_data_churned = pd.DataFrame({'Area Name': unique_values_area_churned, 'Count Churned': count_area_churned})

    # Plan
    unique_values_plan_churned = data['Plan'].unique()
    count_plan_churned = data['Plan'].value_counts()[unique_values_plan_churned]
    plan_data_churned = pd.DataFrame({'Plan': unique_values_plan_churned, 'Count Churned': count_plan_churned})

    # Tv Plan
    unique_values_tvplan_churned = data['Tv Plan'].unique()
    count_tvplan_churned = data['Tv Plan'].value_counts()[unique_values_tvplan_churned]
    tvplan_data_churned = pd.DataFrame({'Tv Plan': unique_values_tvplan_churned, 'Count Churned': count_tvplan_churned})

    # Advance Promo
    unique_values_adv_churned = data['Advance Promo'].unique()
    count_adv_churned = data['Advance Promo'].value_counts()[unique_values_adv_churned]
    adv_data_churned = pd.DataFrame({'Advance Promo': unique_values_adv_churned, 'Count Churned': count_adv_churned})

    # Complaint by Customer Service
    unique_values_com_cs_churned = data['Complaint by Customer Service'].unique()
    count_com_cs_churned = data['Complaint by Customer Service'].value_counts()[unique_values_com_cs_churned]
    com_cs_data_churned = pd.DataFrame({'Complaint by Customer Service': unique_values_com_cs_churned, 'Count Churned': count_com_cs_churned})

    # Complaint by Email
    unique_values_com_e_churned = data['Complaint by Email'].unique()
    count_com_e_churned = data['Complaint by Email'].value_counts()[unique_values_com_e_churned]
    com_e_data_churned = pd.DataFrame({'Complaint by Email': unique_values_com_e_churned, 'Count Churned': count_com_e_churned})

    # Complaint by Social Media
    unique_values_com_socmed_churned = data['Complaint by Social Media'].unique()
    count_com_socmed_churned = data['Complaint by Social Media'].value_counts()[unique_values_com_socmed_churned]
    com_socmed_data_churned = pd.DataFrame({'Complaint by Social Media': unique_values_com_socmed_churned, 'Count': count_com_socmed_churned})

    # Complaint by Telegram
    unique_values_tele_churned = data['Complaint by Telegram'].unique()
    count_tele_churned = data['Complaint by Telegram'].value_counts()[unique_values_tele_churned]
    tele_data_churned = pd.DataFrame({'Complaint by Telegram': unique_values_tele_churned, 'Count Churned': count_tele_churned})

    # Complaint by Whatsapp
    unique_values_wa_churned = data['Complaint by Whatsapp'].unique()
    count_wa_churned = data['Complaint by Whatsapp'].value_counts()[unique_values_wa_churned]
    wa_data_churned = pd.DataFrame({'Complaint by Whatsapp': unique_values_wa_churned, 'Count Churned': count_wa_churned})

    # Complaint by WIC
    unique_values_wic_churned = data['Complaint by WIC'].unique()
    count_wic_churned = data['Complaint by WIC'].value_counts()[unique_values_wic_churned]
    wic_data_churned = pd.DataFrame({'Complaint by WIC': unique_values_wic_churned, 'Count Churned': count_wic_churned})

    return area_data_churned, plan_data_churned, tvplan_data_churned, \
           adv_data_churned, com_cs_data_churned, com_e_data_churned, \
           com_socmed_data_churned, tele_data_churned, wa_data_churned, wic_data_churned


def load_non_churned(data):
    data = data[data['Churn'] == 'Not Churn']
    # Area Name
    unique_values_area_non_churned = data['Area Name'].unique()
    count_area_non_churned = data['Area Name'].value_counts()[unique_values_area_non_churned]
    area_data_non_churned = pd.DataFrame({'Area Name': unique_values_area_non_churned, 'Count Not Churned': count_area_non_churned})

    # Plan
    unique_values_plan_non_churned = data['Plan'].unique()
    count_plan_non_churned = data['Plan'].value_counts()[unique_values_plan_non_churned]
    plan_data_non_churned = pd.DataFrame({'Plan': unique_values_plan_non_churned, 'Count Not Churned': count_plan_non_churned})

    # Tv Plan
    unique_values_tvplan_non_churned = data['Tv Plan'].unique()
    count_tvplan_non_churned = data['Tv Plan'].value_counts()[unique_values_tvplan_non_churned]
    tvplan_data_non_churned = pd.DataFrame({'Tv Plan': unique_values_tvplan_non_churned, 'Count Not Churned': count_tvplan_non_churned})

    # Advance Promo
    unique_values_adv_non_churned = data['Advance Promo'].unique()
    count_adv_non_churned = data['Advance Promo'].value_counts()[unique_values_adv_non_churned]
    adv_data_non_churned = pd.DataFrame({'Advance Promo': unique_values_adv_non_churned, 'Count Not Churned': count_adv_non_churned})

    # Complaint by Customer Service
    unique_values_com_cs_non_churned = data['Complaint by Customer Service'].unique()
    count_com_cs_non_churned = data['Complaint by Customer Service'].value_counts()[unique_values_com_cs_non_churned]
    com_cs_data_non_churned = pd.DataFrame({'Complaint by Customer Service': unique_values_com_cs_non_churned, 'Count Not Churned': count_com_cs_non_churned})

    # Complaint by Email
    unique_values_com_e_non_churned = data['Complaint by Email'].unique()
    count_com_e_non_churned = data['Complaint by Email'].value_counts()[unique_values_com_e_non_churned]
    com_e_data_non_churned = pd.DataFrame({'Complaint by Email': unique_values_com_e_non_churned, 'Count Not Churned': count_com_e_non_churned})

    # Complaint by Social Media
    unique_values_com_socmed_non_churned = data['Complaint by Social Media'].unique()
    count_com_socmed_non_churned = data['Complaint by Social Media'].value_counts()[unique_values_com_socmed_non_churned]
    com_socmed_data_non_churned = pd.DataFrame({'Complaint by Social Media': unique_values_com_socmed_non_churned, 'Count Not Churned': count_com_socmed_non_churned})

    # Complaint by Telegram
    unique_values_tele_non_churned = data['Complaint by Telegram'].unique()
    count_tele_non_churned = data['Complaint by Telegram'].value_counts()[unique_values_tele_non_churned]
    tele_data_non_churned = pd.DataFrame({'Complaint by Telegram': unique_values_tele_non_churned, 'Count Not Churned': count_tele_non_churned})

    # Complaint by Whatsapp
    unique_values_wa_non_churned = data['Complaint by Whatsapp'].unique()
    count_wa_non_churned = data['Complaint by Whatsapp'].value_counts()[unique_values_wa_non_churned]
    wa_data_non_churned = pd.DataFrame({'Complaint by Whatsapp': unique_values_wa_non_churned, 'Count Not Churned': count_wa_non_churned})

    # Complaint by WIC
    unique_values_wic_non_churned = data['Complaint by WIC'].unique()
    count_wic_non_churned = data['Complaint by WIC'].value_counts()[unique_values_wic_non_churned]
    wic_data_non_churned = pd.DataFrame({'Complaint by WIC': unique_values_wic_non_churned, 'Count Not Churned': count_wic_non_churned})

    return area_data_non_churned, plan_data_non_churned, tvplan_data_non_churned, adv_data_non_churned, com_cs_data_non_churned, com_e_data_non_churned, com_socmed_data_non_churned, tele_data_non_churned, wa_data_non_churned, wic_data_non_churned


def visualize_data_batch(data):
    # reverse_data = predict_churn(data)
    # data = reverse_data
    area_data_churned, plan_data_churned, tvplan_data_churned, \
    adv_data_churned, com_cs_data_churned, com_e_data_churned, \
    com_socmed_data_churned, tele_data_churned, wa_data_churned, wic_data_churned = load_churned(data)

    area_data_non_churned, plan_data_non_churned, tvplan_data_non_churned, \
    adv_data_non_churned, com_cs_data_non_churned, com_e_data_non_churned, \
    com_socmed_data_non_churned, tele_data_non_churned, wa_data_non_churned, wic_data_non_churned = load_non_churned(data)

    pdf_path = "Churn Predict.pdf"
    pdf_pages = PdfPages(pdf_path)
    
    area_data_merge = pd.merge(area_data_churned, area_data_non_churned, on="Area Name", how="outer")
    plan_data_merge = pd.merge(plan_data_churned, plan_data_non_churned, on="Plan", how="outer")
    tvplan_data_merge = pd.merge(tvplan_data_churned, tvplan_data_non_churned, on="Tv Plan", how="outer")
    adv_data_merge = pd.merge(adv_data_churned, adv_data_non_churned, on="Advance Promo", how="outer")

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

    option = st.selectbox('Pilih data yang ingin ditampilkan:',
                          ['Area Name', 'Plan', 'Tv Plan', 'Advance Promo'], key= 'piechart_data'
                          )
    # Preprocess the DataFrame by dropping rows with NaN values in 'Count Churned' and 'Count Not Churned' columns
    # Preprocess the DataFrame to handle missing values
    area_data_merge.fillna(0, inplace=True)
    plan_data_merge.fillna(0, inplace=True)
    tvplan_data_merge.fillna(0, inplace=True)
    adv_data_merge.fillna(0, inplace=True)
    
    if option_chart == 'Area Name':
        st.title("Proportion Churn & Not Churn - Area Name")
        # Sort the DataFrame by 'Count Churned' in descending order
        area_data_merge = area_data_merge.sort_values(by='Count Churned', ascending=False)

        # Select the top 5 rows
        top_5 = area_data_merge.head(10)

        # Calculate the sum of 'Count Churned' for the remaining rows
        remaining_sum = area_data_merge.iloc[10:]['Count Churned'].sum()

        # Add the 'dll' row to the DataFrame
        dll_row = {'Area Name': 'dll', 'Count Churned': remaining_sum}
        top_5 = top_5.append(dll_row, ignore_index=True)

        # Plot the pie chart
        plt.figure(figsize=(6, 6))
        patches, texts, autotexts = plt.pie(top_5['Count Churned'], labels=None, autopct='%1.1f%%', startangle=140)
        plt.title('Top 10 Count Churned by Area Name')
        plt.axis('equal')
        
        # Tambahkan legend dengan menggunakan 'Area Name' dari DataFrame 'top_5'
        plt.legend(patches, top_5['Area Name'], loc='best')

        # Display the pie chart using st.pyplot(fig)
        fig = plt.gcf()  # Get the current figure
        st.pyplot(fig)

        # Sort the DataFrame by 'Count Churned' in descending order
        area_data_merge = area_data_merge.sort_values(by='Count Churned', ascending=False)

        # Select the top 5 rows
        top_5 = area_data_merge.head(10)

        # Calculate the sum of 'Count Not Churned' for the remaining rows
        remaining_sum = area_data_merge.iloc[10:]['Count Churned'].sum()

        # Add the 'dll' row to the DataFrame
        dll_row = {'Area Name': 'dll', 'Count Not Churned': remaining_sum}
        top_5 = top_5.append(dll_row, ignore_index=True)

        # Plot the pie chart
        plt.figure(figsize=(6, 6))
        patches, texts, autotexts = plt.pie(top_5['Count Churned'], labels=None, autopct='%1.1f%%', startangle=140)
        plt.title('Top 10 Count Not Churned by Area Name')
        plt.axis('equal')
        
        # Tambahkan legend dengan menggunakan 'Area Name' dari DataFrame 'top_5'
        plt.legend(patches, top_5['Area Name'], loc='best')

        # Display the pie chart using st.pyplot(fig)
        fig = plt.gcf()  # Get the current figure
        st.pyplot(fig)

    # if option == 'Area Name':
    #     # Sort the DataFrame by 'Data Churned' in descending order
    #     area_data_merge = area_data_merge.sort_values(by='Count Churned', ascending=False)

    #     # Select the top 5 rows
    #     top_5 = area_data_merge.head(10)

    #     # Calculate the sum of 'Data Churned' for the remaining rows
    #     remaining_sum = area_data_merge.iloc[10:]['Count Churned'].sum()

    #     # Add the 'dll' row to the DataFrame
    #     dll_row = {'Area Name': 'dll', 'Count Churned': remaining_sum}
    #     top_5 = top_5.append(dll_row, ignore_index=True)

    #     # Plot the pie chart
    #     plt.figure(figsize=(6, 6))
    #     plt.pie(top_5['Count Churned'], labels=None, autopct='%1.1f%%', startangle=140)
    #     plt.title('Top 10 Count Churned by Area Name')
    #     plt.axis('equal')
    #     plt.legend(title="Area Name", loc="best")

    #     # Display the pie chart using st.pyplot(fig)
    #     fig = plt.gcf()  # Get the current figure
    #     st.pyplot(fig)

    #     # Sort the DataFrame by 'Data Churned' in descending order
    #     area_data_merge = area_data_merge.sort_values(by='Count Not Churned', ascending=False)

    #     # Select the top 5 rows
    #     top_5 = area_data_merge.head(10)

    #     # Calculate the sum of 'Data Churned' for the remaining rows
    #     remaining_sum = area_data_merge.iloc[10:]['Count Not Churned'].sum()

    #     # Add the 'dll' row to the DataFrame
    #     dll_row = {'Area Name': 'dll', 'Count Not Churned': remaining_sum}
    #     top_5 = top_5.append(dll_row, ignore_index=True)

    #     # Plot the pie chart
    #     plt.figure(figsize=(6, 6))
    #     plt.pie(top_5['Count Not Churned'], labels=None, autopct='%1.1f%%', startangle=140)
    #     plt.title('Top 10 Count Not Churned by Area Name')
    #     plt.axis('equal')
    #     plt.legend(title="Area Name", loc="best")

    #     # Display the pie chart using st.pyplot(fig)
    #     fig = plt.gcf()  # Get the current figure

    #     st.pyplot(fig)
    elif option == 'Plan':
        # Sort the DataFrame by 'Data Churned' in descending order
        plan_data_merge = plan_data_merge.sort_values(by='Count Churned', ascending=False)

        # Select the top 5 rows
        top_5 = plan_data_merge.head(10)

        # Calculate the sum of 'Data Churned' for the remaining rows
        remaining_sum = plan_data_merge.iloc[10:]['Count Churned'].sum()

        # Add the 'dll' row to the DataFrame
        dll_row = {'Plan': 'dll', 'Count Churned': remaining_sum}
        top_5 = top_5.append(dll_row, ignore_index=True)

        # Plot the pie chart
        plt.figure(figsize=(6, 6))
        plt.pie(top_5['Count Churned'], labels=top_5['Plan'], autopct='%1.1f%%', startangle=140)
        plt.title('Top 10 Count Churned by Plan')
        plt.axis('equal')

        # Display the pie chart using st.pyplot(fig)
        fig = plt.gcf()  # Get the current figure
        st.pyplot(fig)

        # Sort the DataFrame by 'Data Churned' in descending order
        plan_data_merge = plan_data_merge.sort_values(by='Count Not Churned', ascending=False)

        # Select the top 5 rows
        top_5 = plan_data_merge.head(10)

        # Calculate the sum of 'Data Churned' for the remaining rows
        remaining_sum = plan_data_merge.iloc[10:]['Count Not Churned'].sum()

        # Add the 'dll' row to the DataFrame
        dll_row = {'Plan': 'dll', 'Count Not Churned': remaining_sum}
        top_5 = top_5.append(dll_row, ignore_index=True)

        # Plot the pie chart
        plt.figure(figsize=(6, 6))
        plt.pie(top_5['Count Not Churned'], labels=top_5['Plan'], autopct='%1.1f%%', startangle=140)
        plt.title('Top 10 Count Not Churned by Plan')
        plt.axis('equal')

        # Display the pie chart using st.pyplot(fig)
        fig = plt.gcf()  # Get the current figure

        st.pyplot(fig)
    elif option == 'Tv Plan':
        # Sort the DataFrame by 'Data Churned' in descending order
        tvplan_data_merge = tvplan_data_merge.sort_values(by='Count Churned', ascending=False)

        # Select the top 5 rows
        top_5 = tvplan_data_merge.head(10)

        # Calculate the sum of 'Data Churned' for the remaining rows
        remaining_sum = tvplan_data_merge.iloc[10:]['Count Churned'].sum()

        # Add the 'dll' row to the DataFrame
        dll_row = {'Tv Plan': 'dll', 'Count Churned': remaining_sum}
        top_5 = top_5.append(dll_row, ignore_index=True)

        # Plot the pie chart
        plt.figure(figsize=(6, 6))
        plt.pie(top_5['Count Churned'], labels=top_5['Tv Plan'], autopct='%1.1f%%', startangle=140)
        plt.title('Top 10 Count Churned by Plan')
        plt.axis('equal')

        # Display the pie chart using st.pyplot(fig)
        fig = plt.gcf()  # Get the current figure
        st.pyplot(fig)

        # Sort the DataFrame by 'Data Churned' in descending order
        tvplan_data_merge = tvplan_data_merge.sort_values(by='Count Not Churned', ascending=False)

        # Select the top 5 rows
        top_5 = tvplan_data_merge.head(10)

        # Calculate the sum of 'Data Churned' for the remaining rows
        remaining_sum = tvplan_data_merge.iloc[10:]['Count Not Churned'].sum()

        # Add the 'dll' row to the DataFrame
        dll_row = {'Tv Plan': 'dll', 'Count Not Churned': remaining_sum}
        top_5 = top_5.append(dll_row, ignore_index=True)

        # Plot the pie chart
        plt.figure(figsize=(6, 6))
        plt.pie(top_5['Count Not Churned'], labels=top_5['Tv Plan'], autopct='%1.1f%%', startangle=140)
        plt.title('Top 10 Count Not Churned by Plan')
        plt.axis('equal')

        # Display the pie chart using st.pyplot(fig)
        fig = plt.gcf()  # Get the current figure

        st.pyplot(fig)
    elif option == 'Advance Promo':
        # Sort the DataFrame by 'Data Churned' in descending order
        adv_data_merge = adv_data_merge.sort_values(by='Count Churned', ascending=False)

        # Select the top 5 rows
        top_5 = adv_data_merge.head(10)

        # Calculate the sum of 'Data Churned' for the remaining rows
        remaining_sum = adv_data_merge.iloc[10:]['Count Churned'].sum()

        # Add the 'dll' row to the DataFrame
        dll_row = {'Advance Promo': 'dll', 'Count Churned': remaining_sum}
        top_5 = top_5.append(dll_row, ignore_index=True)

        # Plot the pie chart
        plt.figure(figsize=(6, 6))
        plt.pie(top_5['Count Churned'], labels=top_5['Advance Promo'], autopct='%1.1f%%', startangle=140)
        plt.title('Top 10 Count Churned by Plan')
        plt.axis('equal')

        # Display the pie chart using st.pyplot(fig)
        fig = plt.gcf()  # Get the current figure
        st.pyplot(fig)

        # Sort the DataFrame by 'Data Churned' in descending order
        adv_data_merge = adv_data_merge.sort_values(by='Count Not Churned', ascending=False)

        # Select the top 5 rows
        top_5 = adv_data_merge.head(10)

        # Calculate the sum of 'Data Churned' for the remaining rows
        remaining_sum = adv_data_merge.iloc[10:]['Count Not Churned'].sum()

        # Add the 'dll' row to the DataFrame
        dll_row = {'Advance Promo': 'dll', 'Count Not Churned': remaining_sum}
        top_5 = top_5.append(dll_row, ignore_index=True)

        # Plot the pie chart
        plt.figure(figsize=(6, 6))
        plt.pie(top_5['Count Not Churned'], labels=top_5['Advance Promo'], autopct='%1.1f%%', startangle=140)
        plt.title('Top 10 Count Not Churned by Plan')
        plt.axis('equal')

        # Display the pie chart using st.pyplot(fig)
        fig = plt.gcf()  # Get the current figure

        st.pyplot(fig)
    
    st.title("Data Bar Chart Proportion")
    option_chart = st.selectbox('Pilih data yang ingin ditampilkan:',
                          ['Area Name', 'Plan', 'Tv Plan', 'Advance Promo'], key= 'komparasi_churn'
                          )
    unique_area_name = sorted(data['Area Name'].unique())
    area_name_counts = data['Area Name'].value_counts()

    unique_plan = sorted(data['Plan'].unique())
    plan_counts = data['Plan'].value_counts()

    unique_tvplan = sorted(data['Tv Plan'].unique())
    tvplan_counts = data['Tv Plan'].value_counts()

    unique_adv_promo = sorted(data['Advance Promo'].unique())
    adv_promo_counts = data['Advance Promo'].value_counts()

    if option_chart == 'Area Name':
        st.subheader("Proportion Churn & Not Churn - Area Name")
        # Hitung jumlah Churn dan Not Churn untuk setiap area
        churn_counts = data[data['Churn'] == 'Churn']['Area Name'].value_counts()
        not_churn_counts = data[data['Churn'] == 'Not Churn']['Area Name'].value_counts()

        # Membuat dataframe untuk menyimpan hasil perhitungan
        churn_data = pd.DataFrame({'Area Name': unique_area_name,
                                'Churn': [churn_counts.get(area, 0) for area in unique_area_name],
                                'Not Churn': [not_churn_counts.get(area, 0) for area in unique_area_name]})

        # Membuat plot menggunakan sns.catplot
        sns.set(style="whitegrid")
        plt.figure(figsize=(12, 6))
        sns.catplot(x='Area Name', y='value', hue='variable', data=pd.melt(churn_data, ['Area Name']),
                    kind='bar', height=6, aspect=2.5, palette='magma')
        plt.title('Proporsi Churn dan Not Churn berdasarkan Area')
        plt.xlabel('Area Name')
        plt.ylabel('Jumlah')
        plt.xticks(rotation=90)
        st.pyplot(plt)

        # Tampilkan jumlah data churn untuk setiap Area Name
        st.write("Jumlah data churn untuk setiap Area Name:")
        # Membuat dataframe untuk menyimpan hasil perhitungan
        churn_data = pd.DataFrame({'Area Name': unique_area_name,
                                'Churn': [churn_counts.get(area, 0) for area in unique_area_name],
                                'Not Churn': [not_churn_counts.get(area, 0) for area in unique_area_name]})
        st.table(churn_data.head(10))

        if st.button('Download Here - Area Name Proportion Data', key='download_area_name_prop'):
            csv_area_name_prop = churn_data.to_csv(index=False)
            href_not_churned = f'<a href="churn_data:file/csv;charset=utf-8,{csv_area_name_prop}" download="churn_data.csv">Download File CSV</a>'
            st.markdown("Untuk mendownload file seluruh:")
            st.markdown(href_not_churned, unsafe_allow_html=True)
        # for area_name, count in area_name_counts.items():
        #     st.write(f"{area_name}: {count} data churn")

    elif option_chart == 'Plan':
        st.subheader("Proportion Churn & Not Churn - Plan")
        # Hitung jumlah Churn dan Not Churn untuk setiap area
        churn_counts = data[data['Churn'] == 'Churn']['Plan'].value_counts()
        not_churn_counts = data[data['Churn'] == 'Not Churn']['Plan'].value_counts()

        # Membuat dataframe untuk menyimpan hasil perhitungan
        churn_data = pd.DataFrame({'Plan': unique_plan,
                                'Churn': [churn_counts.get(area, 0) for area in unique_plan],
                                'Not Churn': [not_churn_counts.get(area, 0) for area in unique_plan]})

        # Membuat plot menggunakan sns.catplot
        sns.set(style="whitegrid")
        plt.figure(figsize=(12, 6))
        sns.catplot(x='Plan', y='value', hue='variable', data=pd.melt(churn_data, ['Plan']),
                    kind='bar', height=6, aspect=2.5, palette='magma')
        plt.title('Proporsi Churn dan Not Churn berdasarkan Plan')
        plt.xlabel('Plan')
        plt.ylabel('Jumlah')
        plt.xticks(rotation=90)
        st.pyplot(plt)

        # Tampilkan jumlah data churn untuk setiap Plan
        st.write("Jumlah data churn untuk setiap Plan:")
        # Membuat dataframe untuk menyimpan hasil perhitungan
        churn_data = pd.DataFrame({'Plan': unique_plan,
                                'Churn': [churn_counts.get(area, 0) for area in unique_plan],
                                'Not Churn': [not_churn_counts.get(area, 0) for area in unique_plan]})
        st.table(churn_data.head(10))

        if st.button('Download Here - Plan Proportion Data', key='download_plan_prop'):
            csv_plan_prop = churn_data.to_csv(index=False)
            href_not_churned = f'<a href="churn_data:file/csv;charset=utf-8,{csv_plan_prop}" download="churn_data.csv">Download File CSV</a>'
            st.markdown("Untuk mendownload file seluruh:")
            st.markdown(href_not_churned, unsafe_allow_html=True)

    elif option_chart == 'Tv Plan':
        st.subheader("Proportion Churn & Not Churn - Tv Plan")
        # Hitung jumlah Churn dan Not Churn untuk setiap area
        churn_counts = data[data['Churn'] == 'Churn']['Tv Plan'].value_counts()
        not_churn_counts = data[data['Churn'] == 'Not Churn']['Tv Plan'].value_counts()

        # Membuat dataframe untuk menyimpan hasil perhitungan
        churn_data = pd.DataFrame({'Tv Plan': unique_tvplan,
                                'Churn': [churn_counts.get(area, 0) for area in unique_tvplan],
                                'Not Churn': [not_churn_counts.get(area, 0) for area in unique_tvplan]})

        # Membuat plot menggunakan sns.catplot
        sns.set(style="whitegrid")
        plt.figure(figsize=(12, 6))
        sns.catplot(x='Tv Plan', y='value', hue='variable', data=pd.melt(churn_data, ['Tv Plan']),
                    kind='bar', height=6, aspect=2.5, palette='magma')
        plt.title('Proporsi Churn dan Not Churn berdasarkan Tv Plan')
        plt.xlabel('Tv Plan')
        plt.ylabel('Jumlah')
        plt.xticks(rotation=90)
        st.pyplot(plt)

        # Tampilkan jumlah data churn untuk setiap Tv Plan
        st.write("Jumlah data churn untuk setiap Tv Plan:")
        # Membuat dataframe untuk menyimpan hasil perhitungan
        churn_data = pd.DataFrame({'Tv Plan': unique_tvplan,
                                'Churn': [churn_counts.get(area, 0) for area in unique_tvplan],
                                'Not Churn': [not_churn_counts.get(area, 0) for area in unique_tvplan]})
        st.table(churn_data.head(10))

        if st.button('Download Here - Tv Plan Proportion Data', key='download_tvplan_prop'):
            csv_tvplan_prop = churn_data.to_csv(index=False)
            href_not_churned = f'<a href="churn_data:file/csv;charset=utf-8,{csv_tvplan_prop}" download="churn_data.csv">Download File CSV</a>'
            st.markdown("Untuk mendownload file seluruh:")
            st.markdown(href_not_churned, unsafe_allow_html=True)

    elif option_chart == 'Advance Promo':
        st.subheader("Proportion Churn & Not Churn - Advance Promo")
        # Hitung jumlah Churn dan Not Churn untuk setiap area
        churn_counts = data[data['Churn'] == 'Churn']['Advance Promo'].value_counts()
        not_churn_counts = data[data['Churn'] == 'Not Churn']['Advance Promo'].value_counts()

        # Membuat dataframe untuk menyimpan hasil perhitungan
        churn_data = pd.DataFrame({'Advance Promo': unique_adv_promo,
                                'Churn': [churn_counts.get(area, 0) for area in unique_adv_promo],
                                'Not Churn': [not_churn_counts.get(area, 0) for area in unique_adv_promo]})

        # Membuat plot menggunakan sns.catplot
        sns.set(style="whitegrid")
        plt.figure(figsize=(12, 6))
        sns.catplot(x='Advance Promo', y='value', hue='variable', data=pd.melt(churn_data, ['Advance Promo']),
                    kind='bar', height=6, aspect=2.5, palette='magma')
        plt.title('Proporsi Churn dan Not Churn berdasarkan Advance Promo')
        plt.xlabel('Advance Promo')
        plt.ylabel('Jumlah')
        plt.xticks(rotation=90)
        st.pyplot(plt)

        # Tampilkan jumlah data churn untuk setiap Advance Promo
        st.write("Jumlah data churn untuk setiap Advance Promo:")
        # Membuat dataframe untuk menyimpan hasil perhitungan
        churn_data = pd.DataFrame({'Advance Promo': unique_adv_promo,
                                'Churn': [churn_counts.get(area, 0) for area in unique_adv_promo],
                                'Not Churn': [not_churn_counts.get(area, 0) for area in unique_adv_promo]})
        st.table(churn_data.head(10))

        if st.button('Download Here - Tv Plan Proportion Data', key='download_advpromo_prop'):
            csv_advpromo_prop = churn_data.to_csv(index=False)
            href_not_churned = f'<a href="churn_data:file/csv;charset=utf-8,{csv_advpromo_prop}" download="churn_data.csv">Download File CSV</a>'
            st.markdown("Untuk mendownload file seluruh:")
            st.markdown(href_not_churned, unsafe_allow_html=True)

    #Area Data Churned
    area_data_churned = area_data_churned.reset_index(drop=True)
    total = area_data_churned["Count Churned"].sum()
    area_data_churned["Persentase Dari Data Churn"] = area_data_churned["Count Churned"]/total*100
    st.table(area_data_churned.head(10))
    # Menampilkan tombol "Download File CSV"
    if st.button('Download Here - Area Name Churned Data', key='download__area_churned'):
        csv_area_data_churned = data_churned.to_csv(index=False)
        href_churned = f'<a href="area_data_churned:file/csv;charset=utf-8,{csv_data_churned}" download="area_data_churned.csv">Download File CSV</a>'
        st.markdown("Untuk mendownload file seluruh:")
        st.markdown(href_churned, unsafe_allow_html=True)

    #Plan Data Churned
    plan_data_churned = plan_data_churned.reset_index(drop=True)
    total = plan_data_churned["Count Churned"].sum()
    plan_data_churned["Persentase Dari Data Churn"] = plan_data_churned["Count Churned"]/total*100
    st.table(plan_data_churned.head(10))
    # Menampilkan tombol "Download File CSV"
    if st.button('Download Here - Plan Churned Data', key='download__plan_churned'):
        csv_plan_churned = plan_data_churned.to_csv(index=False)
        href_churned = f'<a href="plan_data_churned:file/csv;charset=utf-8,{csv_plan_churned}" download="plan_data_churned.csv">Download File CSV</a>'
        st.markdown("Untuk mendownload file seluruh:")
        st.markdown(href_churned, unsafe_allow_html=True)

    #Tv Plan Data Churned
    tvplan_data_churned = tvplan_data_churned.reset_index(drop=True)
    total = tvplan_data_churned["Count Churned"].sum()
    tvplan_data_churned["Persentase Dari Data Churn"] = tvplan_data_churned["Count Churned"]/total*100
    st.table(tvplan_data_churned.head(10))
    # Menampilkan tombol "Download File CSV"
    if st.button('Download Here - Tv Plan Churned Data', key='download__tv_churned'):
        csv_tvplan_churned = tvplan_data_churned.to_csv(index=False)
        href_churned = f'<a href="tvplan_data_churned:file/csv;charset=utf-8,{csv_tvplan_churned}" download="tvplan_data_churned.csv">Download File CSV</a>'
        st.markdown("Untuk mendownload file seluruh:")
        st.markdown(href_churned, unsafe_allow_html=True)

    #Advance Promo Data Churned
    adv_adv_churned = adv_data_churned.reset_index(drop=True)
    total = adv_data_churned["Count Churned"].sum()
    adv_data_churned["Persentase Dari Data Churn"] = adv_data_churned["Count Churned"]/total*100
    st.table(adv_data_churned.head(10))
    # Menampilkan tombol "Download File CSV"
    if st.button('Download Here - Tv Plan Churned Data', key='download__adv_promo_churned'):
        csv_adv_churned = adv_adv_churned.to_csv(index=False)
        href_churned = f'<a href="adv_adv_churned:file/csv;charset=utf-8,{csv_adv_churned}" download="adv_adv_churned.csv">Download File CSV</a>'
        st.markdown("Untuk mendownload file seluruh:")
        st.markdown(href_churned, unsafe_allow_html=True)

    data_not_churned = data[data['Churn'] == 'Not Churn']
    st.header('Not Churned Data')
    st.table(data_not_churned.head(10))
    # Menampilkan tombol "Download File CSV"
    if st.button('Download Here - Not Churned Data', key='download_not_churned'):
        csv_data_not_churned = data_not_churned.to_csv(index=False)
        href_not_churned = f'<a href="data_not_churned:file/csv;charset=utf-8,{csv_data_not_churned}" download="data_not_churned.csv">Download File CSV</a>'
        st.markdown("Untuk mendownload file seluruh:")
        st.markdown(href_not_churned, unsafe_allow_html=True)

    #Area Data Not Churned
    area_data_non_churned = area_data_non_churned.reset_index(drop=True)
    total = area_data_non_churned["Count Not Churned"].sum()
    area_data_non_churned["Persentase Dari Data Not Churn"] = area_data_non_churned["Count Not Churned"]/total*100
    st.table(area_data_non_churned.head(10))
    # Menampilkan tombol "Download File CSV"
    if st.button('Download Here - Area Not Churned Data', key='download_area_not_churned'):
        csv_area_not_churned = area_data_non_churned.to_csv(index=False)
        href_not_churned = f'<a href="area_data_non_churned:file/csv;charset=utf-8,{csv_area_not_churned}" download="area_data_non_churned.csv">Download File CSV</a>'
        st.markdown("Untuk mendownload file seluruh:")
        st.markdown(href_not_churned, unsafe_allow_html=True)

    #Plan Data Not Churned
    plan_data_non_churned = plan_data_non_churned.reset_index(drop=True)
    total = plan_data_non_churned["Count Not Churned"].sum()
    plan_data_non_churned["Persentase Dari Data Not Churn"] = plan_data_non_churned["Count Not Churned"]/total*100
    st.table(plan_data_non_churned.head(10))
    # Menampilkan tombol "Download File CSV"
    if st.button('Download Here - Plan Not Churned Data', key='download_plan_not_churned'):
        csv_plan_not_churned = plan_data_non_churned.to_csv(index=False)
        href_not_churned = f'<a href="plan_data_non_churned:file/csv;charset=utf-8,{csv_plan_not_churned}" download="plan_data_non_churned.csv">Download File CSV</a>'
        st.markdown("Untuk mendownload file seluruh:")
        st.markdown(href_not_churned, unsafe_allow_html=True)

    #Tv Plan Data Not Churned
    tvplan_data_non_churned = tvplan_data_non_churned.reset_index(drop=True)
    total = tvplan_data_non_churned["Count Not Churned"].sum()
    tvplan_data_non_churned["Persentase Dari Data Not Churn"] = tvplan_data_non_churned["Count Not Churned"]/total*100
    st.table(tvplan_data_non_churned.head(10))
    # Menampilkan tombol "Download File CSV"
    if st.button('Download Here - Tv Plan Not Churned Data', key='download_tvplan_not_churned'):
        csv_tvplan_not_churned = tvplan_data_non_churned.to_csv(index=False)
        href_not_churned = f'<a href="tvplan_data_non_churned:file/csv;charset=utf-8,{csv_tvplan_not_churned}" download="tvplan_data_non_churned.csv">Download File CSV</a>'
        st.markdown("Untuk mendownload file seluruh:")
        st.markdown(href_not_churned, unsafe_allow_html=True)

    #Advance Promo Data Not Churned
    adv_data_non_churned = adv_data_non_churned.reset_index(drop=True)
    total = adv_data_non_churned["Count Not Churned"].sum()
    adv_data_non_churned["Persentase Dari Data Not Churn"] = adv_data_non_churned["Count Not Churned"]/total*100
    st.table(adv_data_non_churned.head(10))
    # Menampilkan tombol "Download File CSV"
    if st.button('Download Here - Advance Promo Not Churned Data', key='download_advpromo_not_churned'):
        csv_advpromo_not_churned = adv_data_non_churned.to_csv(index=False)
        href_not_churned = f'<a href="adv_data_non_churned:file/csv;charset=utf-8,{csv_advpromo_not_churned}" download="adv_data_non_churned.csv">Download File CSV</a>'
        st.markdown("Untuk mendownload file seluruh:")
        st.markdown(href_not_churned, unsafe_allow_html=True)

    # Menghitung jumlah data Churn ##BARUU 18 JULI 2023
    churn_data = data[data['Churn'] == 'Churn']
    st.header("Data Churn")
    st.subheader("Jumlah Data Churn")
    st.table(churn_data.count())

    not_churn_data = data[data['Churn'] == 'Not Churn']
    not_churn_counts = not_churn_data.shape[0]

    st.header("Data Not Churn")
    st.subheader("Jumlah Data Not Churn")
    st.table(not_churn_data.count())

    data_churn = data[data["Churn"] == "Churn"]
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
                                        ('Bali', 'Bandung', 'Bekasi', 'Bogor', 'Cibubur', 'Cilegon', 'Cirebon', 'Depok', 'Jakarta', 'Jambi', 'Karawang', 'Lampung', 'Makassar', 'Malang', 'Medan', 'Palembang', 'Pekanbaru', 'Purwokerto', 'Semarang', 'Serang', 'Solo', 'Surabaya', 'Tangerang', 'Tegal')
                                        )
        user_plan = st.selectbox('Plan', 
                                 ('AMAZING (50 Mbps + TV SD & HD Channels)', 'Alpha 10 Mbps', 'BASIC SUPER (Internet Up To 512 Kbps + TV Channel)', 'BLITZ (Internet Up To 20 Mbps)', 'BSD Basic 10 Mbps', 'BSD Pro 300 Mbps', 'BSD Smash (300 Mbps + TV)', 'BSD Value (100 Mbps + TV)', 'Basic (promo tv booster)', 'Basic 30 Mbps', 'Basic Plus Cosmic', 'Basic Plus Star', 'Basic.15+', 'Basic.8+', 'Basic15', 'Basic15+', 'Basic30+', 'Basic8', 'Bright', 'Business 10 Mbps', 'Business 10 Mbps (free installation fee)', 'Business 100 (PI20)', 'Business 100 (PI21)', 'Business 100 (WEJ)', 'Business 100 Mbps', 'Business 100 Mbps (Promo Buy 1 Get 1)', 'Business 100 Mbps (free installation fee)', 'Business 100Mbps Via Alma', 'Business 20 (PI20)', 'Business 20 (PI21)', 'Business 20 Mbps', 'Business 30 Mbps', 'Business 30 Mbps (free installation fee)', 'Business 300 (PI20)', 'Business 300 (PI21)', 'Business 300 Mbps', 'Business 300 Mbps (Promo Buy 1 Get 1)', 'Business 300 Mbps (free installation fee)', 'Business 50 (PI20)', 'Business 50 (PI21)', 'Business 50 Mbps', 'Business 75 (PI20)', 'Business Pro 100 Mbps', 'Business Pro 150  (PI20)', 'Business Pro 150 (PI21)', 'Business Pro 150 Mbps', 'Business Pro 500 (PI20)', 'Business Pro 500 (PI21)', 'Business Pro 500 Mbps', 'Business Pro 500Mbps Bridge Mode ONT', 'Business.300 Mbps Reg', 'Business.50 Mbps Reg', 'Business100 (PI-22A)', 'Business100 (PI-22B)', 'Business100 Mbps (PA)', 'Business20 (PI-22A)', 'Business20 (PI-22B)', 'Business20 Mbps (PA)', 'Business300 (PI-22A)', 'Business300 (PI-22B)', 'Business300 (PI-22C)', 'Business300 Mbps (PA)', 'Business50 (PI-22A)', 'Business50 (PI-22B)', 'Business50 (PI-22C)', 'Business50 Mbps (PA)', 'BusinessPro 150 Mbps (PA)', 'BusinessPro 500 Mbps (PA)', 'BusinessPro.150 Mbps Reg', 'BusinessPro150 (PI-22A)', 'BusinessPro150 (PI-22B)', 'BusinessPro150 (PI-22C)', 'BusinessPro150 (PI-22D)', 'Demoline PoP 50 Mbps', 'EazyNet (Bonus TV)', 'FESTIVE (40 Mbps + TV SD & HD Channels)', 'FUN (10 Mbps + TV SD & HD Channels)', 'FUN Promo', 'Fantastic300 Mbps New', 'Fast 50 Mbps', 'Fast 50 Mbps+', 'Fast 50 Mbps+ HITS', 'Fast 50 Mbps+ XTRA', 'Fast-50', 'Fast-50 (bit)', 'Fast-50 (fs)', 'Fast-50 (smt)', 'Fast-50 Super93 (1x)', 'Fast-50 Super93 (2x)', 'Fast.50', 'Fast50 (PI-22A)', 'Fast50 (PI-22B)', 'Fast50 (PI-22C)', 'Fast50 (PI-22D)', 'Fast50 (PI-22E)', 'Fast50 (PI-22F)', 'Fast50 (PI-22G)', 'Fast50 (PI-22H)', 'Fast50 (PI-22I)', 'Fast50 (PI-22J)', 'Fast50 (PI-22K)', 'Fast50 (PI-22L)', 'Fast50 (PI20-A)', 'Fast50 (PI20-B)', 'Fast50 (PI21-A)', 'Fast50 (PI21-B)', 'Fast50 (PI21-C)', 'Fast50 (PI21-D)', 'Fast50 (PI21-E)', 'Fast50 Combo', 'Fast50 Combo (PA)', 'Fast50 Combo (PI-22A)', 'Fast50 Combo (PI-22B)', 'Fast50 Combo (PI-22C)', 'Fast50 Combo Anandamaya', 'Fast50 Combo Anandamaya NEW', 'Fast50 Combo Internet A', 'Fast50 Combo Internet A (AP77)', 'Fast50 Combo Internet A (PA 12 Get 12)', 'Fast50 Combo Internet A (PA 12 Get 6)', 'Fast50 Combo Internet A (PA)', 'Fast50 Combo Internet A (PA6)', 'Fast50 Combo New', 'Fast50 Combo New (PA)', 'Fast50 Internet', 'Fast50 Internet (AP77)', 'Fast50 Internet (PA 12 Get 12)', 'Fast50 Internet (PA 12 Get 6)', 'Fast50 Internet (PA)', 'Fast50 Internet (PA3)', 'Fast50 Internet (PA6)', 'Fast50 Mbps', 'Fast50 Mbps (PA)', 'Fast50 Mbps New', 'Fast50 Mbps New (PA)', 'Fast50 Mbps+ Xtra ComboTV', 'Fast50 Special', 'Fast50 Special 2', 'Fast50 Via Alma', 'Fast50+', 'FiberPro 120', 'FiberPro 120 (PI-21)', 'FiberPro 20', 'FiberPro 20 (PI-21)', 'FiberPro 300', 'FiberPro 300 (PI-21)', 'FiberPro 60', 'FiberPro 60 (PI-21)', 'Flash75 ComboTV Pakubuwono', 'GAMER.150+', 'GAMER150+', 'GAMERX50+', 'Gamer (promo tv booster)', 'Gamer 150 Mbps+', 'Gamer 150 Mbps+ XTRA', 'Gamer 150 Mbps+ Xtra ComboTV', 'Gamer 75 Mbps+', 'Gamer 75 Mbps+ XTRA', 'Gamer 75 Mbps+ Xtra ComboTV', 'Gamer-150', 'Gamer-150 (bit)', 'Gamer-150 (fs)', 'Gamer-150 (smt)', 'Gamer-150 Super93 (1x)', 'Gamer-150 Super93 (2x)', 'Gamer150 (PI-22A)', 'Gamer150 (PI-22B)', 'Gamer150 (PI-22C)', 'Gamer150 (PI-22D)', 'Gamer150 (PI20-A)', 'Gamer150 (PI20-B)', 'Gamer150 (PI21-A)', 'Gamer150 (PI21-B)', 'Gamer150 (PI21-C)', 'Gamer150 (PI21-D)', 'Gamer150 Combo', 'Gamer150 Combo (PA)', 'Gamer150 Combo New', 'Gamer150 Combo New (PA)', 'Gamer150 ComboTV Pakubuwono', 'Gamer150 Mbps', 'Gamer150 Mbps New', 'Gamer150 Mbps New (PA)', 'Gamer150 Mbps Reg', 'Gamer150 Mbps Reg (PA)', 'Gamer150 Via Alma', 'Gamer150+ XTRA (PI-22A)', 'Gamer200 Mbps Pakubuwono', 'Gamer50', 'Gamer50 (PI-22A)', 'Gamer50 (PI-22B)', 'Gamer50 (PI-22C)', 'Gamer50 (PI20-A)', 'Gamer50 (PI21-A)', 'GamerX.50+', 'GamerX50', 'Hype75 (PI-22A)', 'Hype75 Combo Internet A', 'Hype75 Combo Internet A (AP77)', 'Hype75 Combo Internet A (PA)', 'Hype75 Combo New', 'Hype75 Combo New (PA)', 'Hype75 Internet', 'Hype75 Internet (AP77)', 'Hype75 Internet (PA)', 'Hype75 Mbps New', 'Hype75 Mbps New (PA)', 'IBS.CA Business 50 Mbps', 'IBS.CA Business 50 Mbps (PI-21)', 'IBS.CA Business Pro 150 Mbps', 'IBS.CA Business100', 'IBS.CA Business100 (PI-21)', 'IBS.CA Business20', 'IBS.CA Business30', 'IBS.CA Business30 (PI-21)', 'IBS.CA Business300', 'IBS.CA Business300 (PI-21)', 'IBS.CA Roket100', 'IBS.CA Roket100 (PI-21)', 'IBS.CA-Fiber120+', 'IBS.CA-Fiber120+ (PI-21)', 'IBS.CA-Fiber60+', 'IBS.CA-Fiber60+ (PI-21)', 'Internet 750Mbps New', 'Internet Up To 3 Mbps', 'Internet Up To 512 Kbps', 'Internet VIP NRO', 'Jet 20 Mbps+', 'Jet 20 Mbps+ HITS', 'Jet 20 PLUS', 'Jet 20 PLUS AP12', 'Jet 20 PLUS AP6', 'Jet-20', 'Jet-20 - winback', 'Jet20', 'Jet20 (PI-22A)', 'Jet20 (PI-22B)', 'Jet20 (PI-22C)', 'Jet20 (PI-22D)', 'Jet20 (PI-22E)', 'Jet20 (PI-22F)', 'Jet20 (PI-22G)', 'Jet20 (PI-22H)', 'Jet20 (PI-22I)', 'Jet20 (PI-22K)', 'Jet20 (PI20-A)', 'Jet20 (PI20-B)', 'Jet20 (PI21-A)', 'Jet20 (PI21-B)', 'Jet20 (PI21-C)', 'Jet20 (PI21-D)', 'Jet20 Combo', 'Jet20 Combo (PA)', 'Jet20 Combo (PI-22A)', 'Jet20 Combo Internet A', 'Jet20 Combo Internet A (PA3)', 'Jet20 Combo Internet A (PA6)', 'Jet20 Combo New', 'Jet20 Internet', 'Jet20 Internet (PA)', 'Jet20 Internet (PA3)', 'Jet20 Internet (PA6)', 'Jet20 Lite', 'Jet20 Mbps', 'Jet20 Mbps (PA)', 'Jet20 Mbps New', 'Jet20 Mbps+ Xtra ComboTV', 'Lite (Package Internet Up To 3 Mbps & TV)', 'Magic Wifi 200', 'Magic Wifi 200 (PI21)', 'MyGamer250 Combo Internet A', 'MyGamer250 Combo Internet A (AP77)', 'MyGamer250 Combo Internet A (PA 12 Get 12)', 'MyGamer250 Combo Internet A (PA 12 Get 6)', 'MyGamer250 Combo Internet A (PA)', 'MyGamer250 Combo Internet A (PA3)', 'MyGamer250 Internet (AP77)', 'MyGamer250 Internet (PA 12 Get 12)', 'MyGamer250 Internet (PA 12 Get 6)', 'MyGamer250 Internet (PA3)', 'MyGamer250 Internet (PA6)', 'MyGamer250 Mbps', 'MyGamer250 Mbps Internet (PA)', 'Nova (promo tv booster)', 'Nova 100 Internet (AP77)', 'Nova 100 Internet (PA 12 Get 6)', 'Nova 100 Internet (PA)', 'Nova 100 Internet (PA3)', 'Nova 100 Internet (PA6)', 'Nova 100 Mbps+', 'Nova 100 Mbps+ HITS', 'Nova 100 Mbps+ XTRA', 'Nova 100 Mbps+ Xtra ComboTV', 'Nova Package', 'Nova Plus Cosmic', 'Nova Plus Star', 'Nova Plus Star (diskon 25% 12 bulan)', 'Nova-100', 'Nova-100 (bit)', 'Nova-100 (fs)', 'Nova-100 (smt)', 'Nova-100 Super93 (1x)', 'Nova-100 Super93 (2x)', 'Nova.100+', 'Nova100 (PI-22A)', 'Nova100 (PI-22B)', 'Nova100 (PI-22C)', 'Nova100 (PI-22D)', 'Nova100 (PI-22E)', 'Nova100 (PI-22F)', 'Nova100 (PI-22G)', 'Nova100 (PI-22H)', 'Nova100 (PI-22I)', 'Nova100 (PI-22J)', 'Nova100 (PI-22L)', 'Nova100 (PI-22M)', 'Nova100 (PI20-A)', 'Nova100 (PI20-B)', 'Nova100 (PI21-A)', 'Nova100 (PI21-B)', 'Nova100 (PI21-C)', 'Nova100 (PI21-D)', 'Nova100 Combo', 'Nova100 Combo (PA)', 'Nova100 Combo (PI-22A)', 'Nova100 Combo (PI-22B)', 'Nova100 Combo Anandamaya', 'Nova100 Combo Internet A', 'Nova100 Combo Internet A (AP77)', 'Nova100 Combo Internet A (PA 12 Get 12)', 'Nova100 Combo Internet A (PA)', 'Nova100 Combo New', 'Nova100 Combo New (PA)', 'Nova100 Internet', 'Nova100 Internet (PA 12 Get 12)', 'Nova100 Mbps', 'Nova100 Mbps Lite', 'Nova100 Mbps Lite (PA)', 'Nova100 Mbps New', 'Nova100 Mbps New (PA)', 'Nova100 Mbps Pakubuwono', 'Nova100 Mbps Pakubuwono Menteng', 'Nova100 Mbps Reg', 'Nova100 Mbps Reg (PA)', 'Nova100 Special', 'Nova100 Via Alma', 'Nova100+', 'Nova150 (PI-22A)', 'Nova150 (PI-22B)', 'Nova150 (PI21-A)', 'Nova150 (PI21-B)', 'Nova150 Combo Anandamaya New', 'Nova150 Mbps Pakubuwono Menteng', 'Nova150 Special', 'Nova150 Special 2', 'Package Internet Up To 10 Mbps & TV Starter 15+', 'Pride 1 Gbps New', 'Prime500 Mbps New', 'Rapid', 'Retain 10Mbps', 'Retain 10Mbps AdvanceTV', 'SNAP (Internet Up To 10 Mbps)', 'SUPER (20 Mbps + TV SD & HD Channels) KOWIS LEWIS', 'SUPER Promo', 'Snap Plus (Bonus TV)', 'Sonic150 Combo', 'Sonic150 Combo (PA)', 'Starter 6 Mbps', 'SuperNova Package', 'SuperNova-300', 'SuperNova-300 (fs)', 'SuperNova300 (PI-21)', 'SuperNova300+', 'Supernova300 ComboTV Pakubuwono', 'Supernova300 Mbps (PA)', 'Supernova400 Mbps Pakubuwono', 'Tanpa Plan', 'Ultra 1 Gbps Combo Internet A', 'Ultra 1Gbps Internet', 'VALUE PROMO', 'VALUE SUPER (Internet Up To 1 Mbps + TV Channel)', 'VIP NRO 2021', 'VIP NRO 2021 (FS)', 'VIP NRO 2021+', 'VIP Rumah Ibadah', 'Value 30 Mbps+', 'Value 30 Mbps+ HITS', 'Value 30 Mbps+ XTRA', 'Value-30', 'Value-30 (bit)', 'Value-30 (fs)', 'Value-30 (smt)', 'Value-30 Super93 (1x)', 'Value-30 Super93 (2x)', 'Value30', 'Value30 (PI-22A)', 'Value30 (PI-22B)', 'Value30 (PI-22C)', 'Value30 (PI-22D)', 'Value30 (PI-22E)', 'Value30 (PI-22F)', 'Value30 (PI-22G)', 'Value30 (PI-22H)', 'Value30 (PI-22I)', 'Value30 (PI-22J)', 'Value30 (PI-22K)', 'Value30 (PI-22M)', 'Value30 (PI-22N)', 'Value30 (PI20-A)', 'Value30 (PI20-B)', 'Value30 (PI21-A)', 'Value30 (PI21-B)', 'Value30 (PI21-C)', 'Value30 (PI21-D)', 'Value30 (PI21-E)', 'Value30 Combo', 'Value30 Combo (PA)', 'Value30 Combo (PI-22A)', 'Value30 Combo (PI-22B)', 'Value30 Combo Internet A', 'Value30 Combo Internet A (AP77)', 'Value30 Combo Internet A (PA 12 Get 12)', 'Value30 Combo Internet A (PA)', 'Value30 Combo Internet A (PA3)', 'Value30 Combo Internet A (PA6)', 'Value30 Combo New', 'Value30 Combo New (PA)', 'Value30 Internet', 'Value30 Internet (AP77)', 'Value30 Internet (PA 12 Get 12)', 'Value30 Internet (PA 12 Get 6)', 'Value30 Internet (PA)', 'Value30 Internet (PA3)', 'Value30 Internet (PA6)', 'Value30 Mbps', 'Value30 Mbps (PA)', 'Value30 Mbps New', 'Value30 Mbps+ Xtra ComboTV', 'Value30 New (PA)', 'Value30 Special', 'Value30 Special 2', 'XTREME (100 Mbps + TV SD & HD Channels)')
                                 )
        
        tv_plan = st.selectbox('TV Plan',
                                  ('Advance TV', 'Advance TV (Android)', 'BASIC', 'Basic TV', 'Combo TV (Fast50)', 'Combo TV (Gamer150)', 'Combo TV (Hype75)', 'Combo TV (Jet20)', 'Combo TV (Nova100)', 'Combo TV (Sonic150)', 'Combo TV (Value30)', 'ComboTV 77 Channel', 'ComboTV Pakubuwono', 'ComboTV Pakubuwono (Android)', 'Cosmic TV', 'Cosmic TV SOHO', 'Fast50 Mbps (ComboTV+ELKMS)', 'Hype75 Mbps (ComboTV+ELKMS)', 'Jet20 Mbps (ComboTV)', 'Local Channel', 'Local Channel (Android)', 'No Channel', 'No Channel (0)', 'Nova100 Mbps (ComboTV+ELKMS)', 'SMARTV', 'SMARTV+', 'SOHO A', 'STAR', 'SmarTV', 'SmarTV+', 'Star TV', 'Star TV Plus', 'Star TV Plus (Android)', 'Star TV SOHO', 'StarTV', 'StarTV Jet', 'TV Only 60 Channel', 'TV SOHO A (News and lifestyle)', 'TV SOHO B (Movies and Sports)', 'TV Starter 15+', 'Tanpa Plan', 'Value30 Mbps (ComboTV+ELK)', 'Xtra ComboTV (Fast50 + ELKMS)', 'Xtra ComboTV (Fast50)', 'Xtra ComboTV (Gamer150)', 'Xtra ComboTV (Gamer75)', 'Xtra ComboTV (Jet20)', 'Xtra ComboTV (Nova100)', 'Xtra ComboTV (V30 + ELK)', 'Xtra ComboTV (Value30)', 'Xtra ComboTV Jet20 (Android)'))
        
        adv_promo = st.selectbox('Advance Promo',
                                 (' Promo Flash Sale 9.9 Value30 Internet ', ' Promo Special Thamrin Residence Disc 20% (6 Bulan) Fast50 Mbps New ', '12 Month Advance Payment (Existing Customer)', '12 Month Advance Payment (New SA)', '3 Month Advance Payment', '3 Months Advance Payment for selected vendor', 'Advance Payment 6 Month', 'Advance Payment Promo 9+3 (After SA)', 'Advance Payment Promo 9+3 (Existing)', 'Advance Payment Promo 9+3 (New SA)', 'Credit Card Payment Reward Discount', 'Credit Card Payment Reward Discount (For Xtra)', 'Disc Demoline PoP 50 Mbps', 'Discount 10000 - PI21 (12Months)', 'Discount 15000 - PI21 (11months)', 'Discount 15000 - PI21 (12months)', 'Discount 30000 - PI21 (11Months)', 'Discount 30000 - PI21 (12Months)', 'Discount 35000 - PI21 (12Months)', 'Discount 40000 - PI21 (11Months)', 'Discount 40000 - PI21 (12Months)', 'Discount VIP NRO (12months)', 'Discount VIP NRO (24months)', 'Discount VIP NRO (36months)', 'Discount VIP NRO (3months)', 'Discount VIP NRO (6months)', 'Discount VIP NRO 2021 (12months)', 'Discount VIP NRO 2021 (24months)', 'Discount VIP NRO 2021 (36months)', 'Discount VIP NRO 2021 (6months)', 'Flash Sale Puri Casablanca Disc 50% (6 Bulan) MyGamer250 Internet', 'Jet20 Mbps Special Discount 20%', 'Jet20 Mbps Special Discount 20% (6 Months)', 'Jet20 Mbps Special Discount 20% - Promo September 2021 (6 Months)', 'Kompensasi Diskon (Disc.10% x 1)', 'Kompensasi Diskon (Disc.10% x 2)', 'Kompensasi Diskon (Disc.10% x 3)', 'Kompensasi Diskon (Disc.15% x 1)', 'Kompensasi Diskon (Disc.15% x 2)', 'Kompensasi Diskon (Disc.15% x 3)', 'Kompensasi Diskon (Disc.20% x 1)', 'Kompensasi Diskon (Disc.20% x 3)', 'Kompensasi Diskon (Disc.25% x 1)', 'Kompensasi Diskon (Disc.25% x 2)', 'Kompensasi Diskon (Disc.25% x 3)', 'Kompensasi Diskon (Disc.50% x 1)', 'Kompensasi Diskon (Disc.50% x 2)', 'Kompensasi Diskon (Disc.50% x 3)', 'New Year 2020 Promo (Bus 100 - 300)', 'New Year 2020 Promo (Bus 50)', 'New Year 2020 Promo (Bus Pro 150 - Pro 500)', 'Nova100 Mbps Reg Discount 30% (for 6 Months)', 'Promo Akhir Tahun - 2021 (All Business)', 'Promo Akhir Tahun - 2021 (All Res)', 'Promo Akhir Tahun - 2021 (Gamer Combo)', 'Promo Akhir Tahun - 2021 (Gamer150 Mbps Reg)', 'Promo Akhir Tahun - 2021 (Nova100 Combo)', 'Promo Akhir Tahun 2022 Disc 20% (12 Bulan) Fast50', 'Promo Akhir Tahun 2022 Disc 20% (12 Bulan) Fast50 Combo A', 'Promo Akhir Tahun 2022 Disc 20% (12 Bulan) MyGamer250', 'Promo Akhir Tahun 2022 Disc 20% (12 Bulan) MyGamer250 Combo A', 'Promo Akhir Tahun 2022 Disc 20% (12 Bulan) Nova100', 'Promo Akhir Tahun 2022 Disc 20% (12 Bulan) Nova100  Combo A', 'Promo CLBK Disc 25% (12 Bulan) Business20 Mbps', 'Promo CLBK Disc 25% (12 Bulan) Business50 Mbps', 'Promo CLBK Disc 25% (12 Bulan) Fast50 Combo A', 'Promo CLBK Disc 25% (12 Bulan) Fast50 Internet', 'Promo CLBK Disc 25% (12 Bulan) Fast50 Mbps New', 'Promo CLBK Disc 25% (12 Bulan) Gamer150 Mbps New', 'Promo CLBK Disc 25% (12 Bulan) Hype75 Internet', 'Promo CLBK Disc 25% (12 Bulan) Hype75 Mbps New', 'Promo CLBK Disc 25% (12 Bulan) Jet20 Combo A', 'Promo CLBK Disc 25% (12 Bulan) Jet20 Internet\t', 'Promo CLBK Disc 25% (12 Bulan) Jet20 Mbps Combo New', 'Promo CLBK Disc 25% (12 Bulan) Jet20 Mbps New', 'Promo CLBK Disc 25% (12 Bulan) MyGamer250 Combo A', 'Promo CLBK Disc 25% (12 Bulan) MyGamer250 Internet', 'Promo CLBK Disc 25% (12 Bulan) Nova100 Combo A', 'Promo CLBK Disc 25% (12 Bulan) Nova100 Internet', 'Promo CLBK Disc 25% (12 Bulan) Nova100 Mbps Combo New', 'Promo CLBK Disc 25% (12 Bulan) Nova100 Mbps New', 'Promo CLBK Disc 25% (12 Bulan) Value30 Combo A', 'Promo CLBK Disc 25% (12 Bulan) Value30 Internet', 'Promo CLBK Disc 25% (12 Bulan) Value30 Mbps Combo New', 'Promo CLBK Disc 25% (12 Bulan) Value30 Mbps New', 'Promo Disc 15% (12 Bulan) Advance Payment', 'Promo Disc 15% (12 Bulan) Business20 Mbps', 'Promo Disc 15% (12 Bulan) Fast50', 'Promo Disc 15% (12 Bulan) Jet20', 'Promo Disc 15% (12 Bulan) Jet20 Combo A', 'Promo Disc 15% (12 Bulan) MyGamer250', 'Promo Disc 15% (12 Bulan) Value30', 'Promo Disc 15% (12 Bulan) Value30 Combo A', 'Promo Disc 20% (12 Bulan) Advance Payment', 'Promo Disc 20% (12 Bulan) Business100 Mbps', 'Promo Disc 20% (12 Bulan) Business100 Mbps + TV', 'Promo Disc 20% (12 Bulan) Business20 Mbps', 'Promo Disc 20% (12 Bulan) Business20 Mbps + TV', 'Promo Disc 20% (12 Bulan) Business300 Mbps', 'Promo Disc 20% (12 Bulan) Business300 Mbps + TV', 'Promo Disc 20% (12 Bulan) Business50 Mbps', 'Promo Disc 20% (12 Bulan) Business50 Mbps + TV', 'Promo Disc 20% (12 Bulan) BusinessPro150 Mbps', 'Promo Disc 20% (12 Bulan) BusinessPro500 Mbps', 'Promo Disc 20% (12 Bulan) Fast50', 'Promo Disc 20% (12 Bulan) Fast50 Combo A', 'Promo Disc 20% (12 Bulan) Fast50 Mbps Combo New', 'Promo Disc 20% (12 Bulan) Fast50 Mbps New', 'Promo Disc 20% (12 Bulan) Gamer150 Mbps Combo New', 'Promo Disc 20% (12 Bulan) Gamer150 Mbps New', 'Promo Disc 20% (12 Bulan) Hype75', 'Promo Disc 20% (12 Bulan) Hype75 Combo A', 'Promo Disc 20% (12 Bulan) Hype75 Mbps Combo New', 'Promo Disc 20% (12 Bulan) Hype75 Mbps New', 'Promo Disc 20% (12 Bulan) Jet20', 'Promo Disc 20% (12 Bulan) Jet20 Combo A', 'Promo Disc 20% (12 Bulan) Jet20 Mbps Combo New', 'Promo Disc 20% (12 Bulan) Jet20 Mbps New', 'Promo Disc 20% (12 Bulan) Nova100', 'Promo Disc 20% (12 Bulan) Nova100  Combo A', 'Promo Disc 20% (12 Bulan) Nova100 Mbps Combo New', 'Promo Disc 20% (12 Bulan) Nova100 Mbps New', 'Promo Disc 20% (12 Bulan) Value30', 'Promo Disc 20% (12 Bulan) Value30 Combo A', 'Promo Disc 20% (12 Bulan) Value30 Mbps Combo New', 'Promo Disc 20% (12 Bulan) Value30 Mbps New', 'Promo Disc 20% 12 Bulan MyGamer250 Mbps', 'Promo Disc 22%+12% (12 Bulan) Advance Payment', 'Promo Disc 25% (12 Bulan) Business100 Mbps', 'Promo Disc 25% (12 Bulan) Business300 Mbps', 'Promo Disc 25% (12 Bulan) Business300 Mbps + TV', 'Promo Disc 25% (12 Bulan) Business50 Mbps', 'Promo Disc 25% (12 Bulan) BusinessPro150 Mbps', 'Promo Disc 25% (12 Bulan) Fast50', 'Promo Disc 25% (12 Bulan) Fast50 Combo A', 'Promo Disc 25% (12 Bulan) Hype75', 'Promo Disc 25% (12 Bulan) Nova100', 'Promo Disc 25% (12 Bulan) Nova100  Combo A', 'Promo Disc 25% (12 Bulan) Value30', 'Promo Disc 25% (12 Bulan) Value30 Combo A', 'Promo Disc 30% (12 Bulan) MyGamer250', 'Promo Disc 30% (12 Bulan) Nova100', 'Promo Disc20% 12 Bulan MyGamer250 Combo A', 'Promo Diskon Khusus Apartment Via Alma (100%)', 'Promo Dismantle 25% (Fast50 Mbps, Fast50 Combo, Business 50)', 'Promo HRB YES Disc 30% Fast50 Combo A', 'Promo HRB YES Disc 30% Fast50 Internet (3 Bulan)', 'Promo HRB YES Disc 30% MyGamer250 Combo A', 'Promo HRB YES Disc 30% MyGamer250 Internet (3 Bulan)', 'Promo HRB YES Disc 30% Nova100 Internet (3 Bulan)', 'Promo HRB YES Disc 30% Value30 Combo A', 'Promo HRB YES Disc 30% Value30 Internet (3 Bulan)', 'Promo Harbolnas September Fast50 Combo A', 'Promo Harbolnas September Fast50 Internet', 'Promo Harbolnas September MyGamer250 Combo A', 'Promo Harbolnas September MyGamer250 Internet', 'Promo Harbolnas September Nova100 Combo A', 'Promo Harbolnas September Nova100 Internet', 'Promo Harbolnas September Value30 Combo A', 'Promo Harbolnas September Value30 Internet', 'Promo Hari Pahlawan - 2021 (All Res)', 'Promo Hari Pahlawan - 2021 (Gamer Combo)', 'Promo Hari Pahlawan - 2021 (Sonic)', 'Promo Imlek Disc 15% (6 Bulan) Hype 75 Mbps New', 'Promo Imlek Disc 25% (6 Bulan)  Gamer 150 Mbps New', 'Promo Imlek Disc 25% (6 Bulan)  Nova 100 Mbps Combo New ', 'Promo Imlek Disc 25% (6 Bulan)  Nova 100 Mbps New ', 'Promo Internet VIP Rumah Ibadah', 'Promo Merdeka Disc 25% 6 Bulan (MyGamer250 Combo A)', 'Promo Merdeka Disc 25% 6 Bulan (MyGamer250)', 'Promo Merdeka Disc 25% 6 Bulan (Nova100 Combo A)', 'Promo Merdeka Disc 25% 6 Bulan (Nova100)', 'Promo MyRep YES Fast50 Combo A', 'Promo MyRep YES Fast50 Internet', 'Promo MyRep YES MyGamer250 Combo A', 'Promo MyRep YES MyGamer250 Internet', 'Promo MyRep YES Nova100 Combo A', 'Promo MyRep YES Nova100 Internet', 'Promo MyRep YES Value30 Combo A', 'Promo MyRep YES Value30 Internet', 'Promo Nasional (Disc 15% 6 Bulan) MyGamer250 Combo A', 'Promo Nasional (Disc 15% 6 Bulan) MyGamer250 Mbps', 'Promo Nasional 2022 Disc 15% (6 Bulan) Gamer150 Mbps Combo New', 'Promo Nasional 2022 Disc 15% (6 Bulan) Gamer150 Mbps New', 'Promo Nasional 2022 Disc 15% (6 Bulan) Nova100 Mbps Combo New', 'Promo Nasional 2022 Disc 15% (6 Bulan) Nova100 Mbps New', 'Promo Nasional 2023 (PA 5 Get 1) Fast50', 'Promo Nasional 2023 (PA 5 Get 1) Fast50 Combo Internet A', 'Promo Nasional 2023 (PA 5 Get 1) Jet20', 'Promo Nasional 2023 (PA 5 Get 1) MyGamer250', 'Promo Nasional 2023 (PA 5 Get 1) Nova100', 'Promo Nasional 2023 (PA 5 Get 1) Value30', 'Promo Nasional 2023 (PA 5 Get 1) Value30 Combo Internet A', 'Promo Nasional 2023 Disc. 15% (12 Bulan) Jet20', 'Promo Nasional 2023 Disc. 15% (12 Bulan) Jet20 Combo A', 'Promo Nasional 2023 Disc. 15% (12 Bulan) Value30', 'Promo Nasional 2023 Disc. 15% (12 Bulan) Value30 Combo A', 'Promo Nasional 2023 Disc. 20% (12 Bulan) Fast50', 'Promo Nasional 2023 Disc. 20% (12 Bulan) Fast50 Combo A', 'Promo Nasional 2023 Disc. 25% (12 Bulan) MyGamer250', 'Promo Nasional 2023 Disc. 25% (12 Bulan) MyGamer250 Combo A', 'Promo Nasional 2023 Disc. 25% (12 Bulan) Nova100', 'Promo Nasional 2023 Disc. 25% (12 Bulan) Nova100 Combo A', 'Promo Nasional Disc 15% 6 Bulan (Nova100 Combo A)', 'Promo Nasional Disc 15% 6 Bulan (Nova100)', 'Promo New Area (Fast50 Mbps Combo New) 12 bulan', 'Promo New Area (Fast50 Mbps Combo New) 6 bulan', 'Promo New Area (Fast50 Mbps New) 12 bulan', 'Promo New Area (Fast50 Mbps New) 6 bulan', 'Promo New Area (Gamer150 Combo New) 12 Bulan', 'Promo New Area (Gamer150 New) 6 Bulan', 'Promo New Area (Hype75 Mbps New) 12 bulan', 'Promo New Area (Hype75 Mbps New) 6 bulan', 'Promo New Area (Nova100 Combo New) 12 Bulan', 'Promo New Area (Nova100 New) 12 Bulan', 'Promo New Area (Nova100 New) 6 Bulan', 'Promo New Area (Value30 Mbps Combo New) 12 bulan', 'Promo New Area (Value30 Mbps Combo New) 6 bulan', 'Promo New Area (Value30 Mbps New) 12 bulan', 'Promo New Area (Value30 Mbps New) 6 bulan', 'Promo New Area Disc 20% (12 Bulan) Business20 Mbps', 'Promo New Area Disc 20% (12 Bulan) Business20 Mbps + TV', 'Promo New Area Disc 20% (12 Bulan) Fast50 Mbps Combo New', 'Promo New Area Disc 20% (12 Bulan) Fast50 Mbps New', 'Promo New Area Disc 20% (12 Bulan) Gamer150 Mbps Combo New', 'Promo New Area Disc 20% (12 Bulan) Gamer150 Mbps New', 'Promo New Area Disc 20% (12 Bulan) Hype75 Mbps New', 'Promo New Area Disc 20% (12 Bulan) Jet20 Mbps Combo New', 'Promo New Area Disc 20% (12 Bulan) Jet20 Mbps New', 'Promo New Area Disc 20% (12 Bulan) Nova100 Mbps Combo New', 'Promo New Area Disc 20% (12 Bulan) Nova100 Mbps New', 'Promo New Area Disc 20% (12 Bulan) Value30 Mbps Combo New', 'Promo New Area Disc 20% (12 Bulan) Value30 Mbps New', 'Promo New RFS Disc 15% Jet20 Mbps Combo New', 'Promo New RFS Disc 15% Jet20 Mbps New', 'Promo New RFS Disc 15% Value30 Mbps Combo New', 'Promo New RFS Disc 15% Value30 Mbps New', 'Promo New RFS Disc 25% Fast50 Mbps Combo New', 'Promo New RFS Disc 25% Fast50 Mbps New', 'Promo New RFS Disc 25% Gamer150 Mbps New ', 'Promo New RFS Disc 25% Hype75 Mbps New', 'Promo New RFS Disc 25% Nova100 Mbps New', 'Promo New RFS HRB Disc 15% (6 Bulan) MyGamer250 Internet', 'Promo New RFS HRB Disc 15% (6 Bulan) Nova100 Combo A', 'Promo New RFS HRB Disc 15% (6 Bulan) Nova100 Internet', 'Promo New RFS HRB Disc 15% (6 Bulan) Value30 Internet', 'Promo New RFS HRB Disc 20% (6 Bulan) Fast50', 'Promo New RFS HRB Disc 20% (6 Bulan) Fast50 Combo A', 'Promo New RFS HRB Disc 20% (6 Bulan) MyGamer250 Mbps', 'Promo New RFS HRB Disc 20% (6 Bulan) Nova100 ', 'Promo New RFS HRB Disc 20% (6 Bulan) Nova100 Combo A', 'Promo New RFS HRB MyGamer250 Mbps', 'Promo New RFS Lampung dan Pekanbaru  (Disc 25% 12 Bulan)  MyGamer250 Combo A', 'Promo New RFS Lampung dan Pekanbaru  (Disc 25% 12 Bulan)  MyGamer250 Mbps', 'Promo New RFS Pekanbaru Disc 15% Jet20 Mbps Combo New', 'Promo New RFS Pekanbaru Disc 15% Jet20 Mbps New', 'Promo New Year New Value (Advance Payment)', 'Promo New Year New Value Combo', 'Promo New Year New Value Internet', 'Promo Oktober 2022 Disc 25% (12 Bulan) Fast50 Combo A', 'Promo Oktober 2022 Disc 25% (12 Bulan) Fast50 Internet', 'Promo Oktober 2022 Disc 25% (12 Bulan) MyGamer250 Combo A', 'Promo Oktober 2022 Disc 25% (12 Bulan) MyGamer250 Internet', 'Promo Oktober 2022 Disc 25% (12 Bulan) Nova100 Combo A', 'Promo Oktober 2022 Disc 25% (12 Bulan) Nova100 Internet', 'Promo Ramadhan - Idul Fitri Disc 20% (12 Bulan) Fast50 Mbps Combo New', 'Promo Ramadhan - Idul Fitri Disc 20% (12 Bulan) Fast50 Mbps New', 'Promo Ramadhan - Idul Fitri Disc 20% (12 Bulan) Gamer150 Mbps Combo New', 'Promo Ramadhan - Idul Fitri Disc 20% (12 Bulan) Gamer150 Mbps New', 'Promo Ramadhan - Idul Fitri Disc 20% (12 Bulan) Hype75 Mbps Combo New', 'Promo Ramadhan - Idul Fitri Disc 20% (12 Bulan) Hype75 Mbps New', 'Promo Ramadhan - Idul Fitri Disc 20% (12 Bulan) Nova100 Mbps Combo New', 'Promo Ramadhan - Idul Fitri Disc 20% (12 Bulan) Nova100 Mbps New', 'Promo Ramadhan Up to 30% 2021 (Fast50 Combo, Gamer150 Mbps, Gamer150 Combo)', 'Promo Ramadhan Up to 30% 2021 (Fast50 Mbps)', 'Promo Ramadhan Up to 30% 2021 (Nova100 Mbps, Nova100 Combo, Sonic150 Combo)', 'Promo Ruko Special Price Disc 15% (6 Bulan) Fast50 Internet', 'Promo Ruko Special Price Disc 15% (6 Bulan) FiberPro20', 'Promo Ruko Special Price Disc 15% (6 Bulan) FiberPro60', 'Promo Ruko Special Price Disc 15% (6 Bulan) Jet20 Combo A', 'Promo Ruko Special Price Disc 15% (6 Bulan) Jet20 Internet', 'Promo Ruko Special Price Disc 15% (6 Bulan) MyGamer250 Internet', 'Promo Ruko Special Price Disc 15% (6 Bulan) Nova100 Internet', 'Promo Ruko Special Price Disc 15% (6 Bulan) Value30 Internet', 'Promo Shocktober Disc 25% (12 Bulan) Jet20', 'Promo Shocktober Disc 25% (12 Bulan) Jet20 Combo A', 'Promo Shocktober Disc 25% (12 Bulan) Value30 Combo A', 'Promo Shocktober Disc 25% (12 Bulan) Value30 Internet', 'Promo Shocktober Disc 30% (12 Bulan) Fast50 Combo A', 'Promo Shocktober Disc 30% (12 Bulan) Fast50 Internet', 'Promo Shocktober Disc 30% (12 Bulan) MyGamer250 Combo A', 'Promo Shocktober Disc 30% (12 Bulan) MyGamer250 Internet', 'Promo Shocktober Disc 30% (12 Bulan) Nova100 Combo A', 'Promo Shocktober Disc 30% (12 Bulan) Nova100 Internet', 'Promo Sinarmas Employee', 'Promo Special Fast50 Combo Disc 25% 12 Bulan', 'Promo Special Fast50 Mbps Disc 25% 12 Bulan', 'Promo Special Thamrin Residence Disc 20% (6 Bulan) Gamer150 Combo New', 'Promo Special Thamrin Residence Disc 20% (6 Bulan) Hype75 Mbps New', 'Promo Special Thamrin Residence Disc 20% (6 Bulan) Nova100 Mbps New ', 'Promo Sumpah Pemuda - 2021 (All Res)', 'Promo Switching 2022 Disc 30% (12 Bulan) Fast50 Mbps Combo New', 'Promo Switching 2022 Disc 30% (12 Bulan) Fast50 Mbps New', 'Promo Switching 2022 Disc 30% (12 Bulan) Gamer150 Mbps Combo New', 'Promo Switching 2022 Disc 30% (12 Bulan) Gamer150 Mbps New', 'Promo Switching 2022 Disc 30% (12 Bulan) Hype75 Mbps Combo New', 'Promo Switching 2022 Disc 30% (12 Bulan) Hype75 Mbps New', 'Promo Switching 2022 Disc 30% (12 Bulan) Jet20 Mbps Combo New', 'Promo Switching 2022 Disc 30% (12 Bulan) Jet20 Mbps New', 'Promo Switching 2022 Disc 30% (12 Bulan) Nova100 Mbps Combo New', 'Promo Switching 2022 Disc 30% (12 Bulan) Nova100 Mbps New', 'Promo Switching 2022 Disc 30% (12 Bulan) Value30 Mbps Combo New', 'Promo Switching 2022 Disc 30% (12 Bulan) Value30 Mbps New', 'Promo Tahun Baru Disc 25% (6 Bulan)  Gamer 150 Mbps Combo New', 'Promo Tahun Baru Disc 25% (6 Bulan)  Gamer 150 Mbps New', 'Promo Tahun Baru Disc 25% (6 Bulan)  Gamer 150 Mbps New ', 'Promo Tahun Baru Disc 25% (6 Bulan)  Nova 100 Mbps Combo New', 'Promo Tahun Baru Disc 25% (6 Bulan) Nova 100 Mbps New', 'Promo Tahun Baru Disc 25% (6 Bulan) Nova 100 Mbps New ', 'Promo Thamrin Residence Disc 20% (6 Bulan) Fast50', 'Promo Thamrin Residence Disc 20% (6 Bulan) Fast50 Combo A', 'Promo Thamrin Residence Disc 20% (6 Bulan) Hype75', 'Promo Thamrin Residence Disc 20% (6 Bulan) Hype75 Combo A', 'Promo Thamrin Residence Disc 20% (6 Bulan) Nova100 ', 'Promo Thamrin Residence MyGamer250 Combo A', 'Promo Thamrin Residence MyGamer250 Mbps', 'Promo Ultah MyRep Disc 20% + 7% (12 Bulan) Fast50 Mbps Combo New', 'Promo Ultah MyRep Disc 20% + 7% (12 Bulan) Fast50 Mbps New', 'Promo Ultah MyRep Disc 20% + 7% (12 Bulan) Gamer150 Mbps Combo New', 'Promo Ultah MyRep Disc 20% + 7% (12 Bulan) Gamer150 Mbps New', 'Promo Ultah MyRep Disc 20% + 7% (12 Bulan) Hype75 Mbps Combo New', 'Promo Ultah MyRep Disc 20% + 7% (12 Bulan) Hype75 Mbps New', 'Promo Ultah MyRep Disc 20% + 7% (12 Bulan) Nova100 Mbps Combo New', 'Promo Ultah MyRep Disc 20% + 7% (12 Bulan) Nova100 Mbps New', 'Promo Upsell  Disc 15% (6 Bulan) Fast50', 'Promo Upsell  Disc 15% (6 Bulan) Hype75', 'Promo Upsell  Disc 15% (6 Bulan) Nova100', 'Promo Upsell  Disc 15% (6 Bulan) Value30', 'Promo Upsell (Disc 15% 6 Bulan) MyGamer250 Combo A', 'Promo Upsell (Disc 15% 6 Bulan) MyGamer250 Mbps', 'Promo Upsell 15% (Fast50 Mbps Combo New) 6 bulan', 'Promo Upsell 15% (Fast50 Mbps New) 6 bulan', 'Promo Upsell 15% (Gamer150 Combo New) 6 Bulan', 'Promo Upsell 15% (Gamer150 New) 6 Bulan', 'Promo Upsell 15% (Hype75 Mbps Combo New) 6 bulan', 'Promo Upsell 15% (Hype75 Mbps New) 6 bulan', 'Promo Upsell 15% (Nova100 New) 6 Bulan', 'Promo Upsell 15% (Value30 Mbps Combo New) 6 bulan', 'Promo Upsell 15% (Value30 Mbps New) 6 bulan', 'Promo Upsell Disc 15% (6 Bulan) Fast50 Combo A', 'Promo Upsell Disc 15% (6 Bulan) Hype75 Combo A', 'Promo Upsell Disc 15% (6 Bulan) Nova100 Combo A', 'Promo Upsell Disc 15% (6 Bulan) Value30 Combo A', 'Promo WOW FLASH SALE Fast50 Combo A', 'Promo WOW FLASH SALE Fast50 Internet', 'Promo WOW FLASH SALE MyGamer250 Combo A', 'Promo WOW FLASH SALE MyGamer250 Internet', 'Promo WOW FLASH SALE Nova100 Combo A', 'Promo WOW FLASH SALE Nova100 Internet', 'Promo WOW FLASH SALE Value30 Combo A', 'Promo WOW FLASH SALE Value30 Internet', 'Promo WOW-VEMBER DEALS Fast50 Combo A', 'Promo WOW-VEMBER DEALS Fast50 Internet', 'Promo WOW-VEMBER DEALS MyGamer250 Combo A', 'Promo WOW-VEMBER DEALS MyGamer250 Internet', 'Promo WOW-VEMBER DEALS Nova100 Combo A', 'Promo WOW-VEMBER DEALS Nova100 Internet', 'Promo WOW-VEMBER DEALS Value30 Combo A', 'Promo WOW-VEMBER DEALS Value30 Internet', 'RWB Promo Diskon 10% x 3 ', 'RWB Promo Diskon 25% X 3', 'RWB Promo Diskon 25% X 6', 'RWB Promo Diskon 35%', 'RWB Promo Diskon 35% X 6', 'RWB Promo Diskon 50% X 3', 'RWB Promo Diskon 50% X 6', 'Tanpa Advance Promo', 'Upsell Discount (20% 3 Months)')
                                )
        
        comp_cs = st.slider('Complaint by Customer Service', min_value = 0.0, max_value = 200.0 ,step=1.0)
        comp_email = st.slider('Complaint by Email', min_value = 0.0, max_value = 250.0 ,step=1.0)
        comp_socmed = st.slider('Complaint by Social Media', min_value = 0.0, max_value = 200.0 ,step=1.0)
        comp_tel = st.slider('Complaint by Telegram', min_value = 0.0, max_value = 100.0 ,step=1.0)
        comp_wa = st.slider('Complaint by Whatsapp', min_value = 0.0, max_value = 400.0 ,step=1.0)
        comp_wic = st.slider('Complaint by WIC', min_value = 0.0, max_value = 150.0 ,step=1.0)
        
        user_df_data = [[user_area,user_plan,tv_plan,adv_promo,comp_cs,comp_email,comp_socmed,comp_tel,comp_wa,comp_wic]]
        user_df_colnames = ["Area Name","Plan","Tv Plan","Advance Promo","Complaint by Customer Service","Complaint by Email","Complaint by Social Media","Complaint by Telegram","Complaint by Whatsapp","Complaint by WIC"]

        if st.button("Predict"):
            input_df = pd.DataFrame(user_df_data,columns = user_df_colnames)
            data, reverse_data = predict_churn(input_df)
            churn_value = reverse_data.iloc[0]['Churn']

            if churn_value == "Not Churn":
                st.success('The customer will Not Churn.')
            elif churn_value == "Churn":
                st.success('The customer will Churn.')

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