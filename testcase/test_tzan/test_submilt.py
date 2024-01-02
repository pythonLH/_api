import requests
import json

url = "http://192.168.122.151:8065/aPiTzA/hc/app/market/submitOneProduct"

payload = json.dumps({
  "customerSource": "com.example.myapplication",
  "promotionChannels": "googlePlay",
  "appVersionCode": "1",
  "sign": {
    "BqCRU": "0",
    "CFeTVY": "0",
    "ChDe": "",
    "CmgkNmG": "8",
    "FhOTz": "STK-L23BHN",
    "FoIBgMy": "REL",
    "FsCnhR": "",
    "GEdqeft": "1",
    "HPzDje": "2224",
    "IMVrG": "1325000KHz",
    "IMxSgU": "HONOR 9",
    "Jci": "34",
    "KPDvdWP": "0",
    "KYoRA": "arm64-v8a",
    "KsMNHZO": "",
    "MJu": "112.9199GB",
    "MMMAPKN": "1080",
    "NWZ": "",
    "OhV": "97.4021GB",
    "PcqiU": "1.2135GB",
    "PnBQ": "02:00:00:00:00:00",
    "QFCX": "wifi",
    "QxzS": "",
    "RFeF": "3.5937GB",
    "RIoeQJC": "1080,2224",
    "SOOT": "HUAWEI#STK-LX3",
    "SRI": "kirin710",
    "TCeK": "",
    "TIM": "0.3682GB",
    "TvkaJY": "1080,2224",
    "UDUcmS": "",
    "Yud": "2023-10-17 17:17:05",
    "Zox": "21C20B388S000C000,21C20B388S000C000",
    "ayp": "0",
    "eEyFIN": "",
    "evhFkS": "0.3750GB",
    "hbJuCuK": "6f3fffbb57656c60045dbe4970da6ce760cd52cd2eb8b181257c42935b16cd09",
    "hduo": "0",
    "jCcOHX": "",
    "jcYaR": "user",
    "jychsv": " Hisilicon Kirin710",
    "kTlQlVg": "f7a94067-19ba-449c-89a7-26f46c3d4bd5",
    "lCpQWNc": "",
    "lbC": "Android",
    "nEWFgiB": "75",
    "qIO": "HUAWEI#STK-LX3",
    "qece": "GMT+08:00",
    "rjQ": "04:8C:9A:C9:B7:DF",
    "rpCZILM": "zh",
    "ruN": "10",
    "sEjkl": "881ed329f71a483f",
    "tVocSYN": "255",
    "tbBT": "[111, 63, -1, -69, 87, 101, 108, 96, 4, 93, -66, 73, 112, -38, 108, -25, 96, -51, 82, -51, 46, -72, -79, -127, 37, 124, 66, -109, 91, 22, -51, 9]",
    "tzlyfy": "",
    "ugqaU": "0",
    "uuk": "",
    "wXZ": "HONOR/STK-L23BHN/HWSTK-HF:10/HONORSTK-LX3/10.0.0.231C636:user/release-keys",
    "wuuifx": "0",
    "xHljj": ""
  },
  "appList": [
    {
      "DUkSAIO": "com.agoda.mobile.consumer",
      "ZOaSHz": "2018-08-08 00:01:00",
      "dDFfR": "11.39.1",
      "eGgOeO": "2023-10-07 09:45:03",
      "sBRGsP": "186640",
      "sjzCfH": "Agoda安可达"
    },
    {
      "DUkSAIO": "com.dineroexpreso.app",
      "ZOaSHz": "2023-10-20 15:12:37",
      "dDFfR": "1.0.0",
      "eGgOeO": "2023-10-20 15:12:37",
      "sBRGsP": "100",
      "sjzCfH": "Dinero Expreso"
    },
    {
      "DUkSAIO": "com.alibaba.aliexpresshd",
      "ZOaSHz": "2022-06-16 21:58:38",
      "dDFfR": "6.12.1",
      "eGgOeO": "2022-06-16 21:58:38",
      "sBRGsP": "226",
      "sjzCfH": "AliExpress"
    },
    {
      "DUkSAIO": "com.google.android.apps.docs.editors.docs",
      "ZOaSHz": "2018-08-08 00:01:00",
      "dDFfR": "1.18.412.02.40",
      "eGgOeO": "2018-08-08 00:01:00",
      "sBRGsP": "184120240",
      "sjzCfH": "文档"
    },
    {
      "DUkSAIO": "prestamos.creditoya.urgente.dinero.peso.cash.credito.rapido",
      "ZOaSHz": "2022-07-18 11:13:04",
      "dDFfR": "1.3.0",
      "eGgOeO": "2022-07-18 11:13:04",
      "sBRGsP": "1003000",
      "sjzCfH": "CreditoYa"
    },
    {
      "DUkSAIO": "com.latin.pe.hinance",
      "ZOaSHz": "2023-10-16 14:57:14",
      "dDFfR": "1.2.2",
      "eGgOeO": "2023-10-16 14:57:14",
      "sBRGsP": "122",
      "sjzCfH": "Préstamo con tranquilidad"
    },
    {
      "DUkSAIO": "com.google.android.apps.docs.editors.sheets",
      "ZOaSHz": "2018-08-08 00:01:00",
      "dDFfR": "1.18.412.03.40",
      "eGgOeO": "2018-08-08 00:01:00",
      "sBRGsP": "184120340",
      "sjzCfH": "表格"
    },
    {
      "DUkSAIO": "com.google.android.apps.docs.editors.slides",
      "ZOaSHz": "2018-08-08 00:01:00",
      "dDFfR": "1.18.412.02.40",
      "eGgOeO": "2018-08-08 00:01:00",
      "sBRGsP": "184120240",
      "sjzCfH": "幻灯片"
    },
    {
      "DUkSAIO": "mex.af.test",
      "ZOaSHz": "2023-01-19 10:53:11",
      "dDFfR": "1.0.0",
      "eGgOeO": "2023-01-19 10:53:11",
      "sBRGsP": "1",
      "sjzCfH": "SoloCash"
    },
    {
      "DUkSAIO": "ng.personal.loan.lily.cash",
      "ZOaSHz": "2020-08-08 10:40:47",
      "dDFfR": "Li1.0.2",
      "eGgOeO": "2020-08-08 10:40:56",
      "sBRGsP": "102",
      "sjzCfH": "Lilycash"
    },
    {
      "DUkSAIO": "com.dinero.urgente.mexican",
      "ZOaSHz": "2023-08-16 15:00:20",
      "dDFfR": "1.1.5",
      "eGgOeO": "2023-08-16 15:00:20",
      "sBRGsP": "115",
      "sjzCfH": "Dinero urgente"
    },
    {
      "DUkSAIO": "com.loan.credit.branch.tala.fast.efectivo.mexico",
      "ZOaSHz": "2022-07-14 18:02:06",
      "dDFfR": "1.5.6",
      "eGgOeO": "2022-07-14 18:02:06",
      "sBRGsP": "208",
      "sjzCfH": "iFectivo"
    },
    {
      "DUkSAIO": "com.palmpocket.cash.loan.app",
      "ZOaSHz": "2022-07-18 11:08:07",
      "dDFfR": "1.1.3",
      "eGgOeO": "2022-07-18 11:08:07",
      "sBRGsP": "14",
      "sjzCfH": "PalmPocket"
    },
    {
      "DUkSAIO": "com.koushikdutta.vysor",
      "ZOaSHz": "2023-08-02 18:56:11",
      "dDFfR": "4.2.2",
      "eGgOeO": "2023-08-02 18:56:11",
      "sBRGsP": "1690902000",
      "sjzCfH": "Vysor"
    },
    {
      "DUkSAIO": "credit.prestamos.personale.cash.efectivo",
      "ZOaSHz": "2022-07-14 18:01:25",
      "dDFfR": "1.0.77",
      "eGgOeO": "2022-07-14 18:01:25",
      "sBRGsP": "77",
      "sjzCfH": "Superapoyo"
    },
    {
      "DUkSAIO": "com.prestamo.facil.pe",
      "ZOaSHz": "2023-09-17 11:07:07",
      "dDFfR": "1.0.4",
      "eGgOeO": "2023-09-17 11:07:07",
      "sBRGsP": "104",
      "sjzCfH": "Préstamo Fácil"
    },
    {
      "DUkSAIO": "com.potplayer.pot.videoplayer.allformatplayer.app",
      "ZOaSHz": "2023-07-21 15:45:48",
      "dDFfR": "2.0",
      "eGgOeO": "2023-07-21 15:45:48",
      "sBRGsP": "2",
      "sjzCfH": "Pot Player"
    },
    {
      "DUkSAIO": "com.kenya.credit.app.loan.cash.money.pesa",
      "ZOaSHz": "2022-07-19 21:31:09",
      "dDFfR": "1.0.9",
      "eGgOeO": "2022-07-19 21:31:09",
      "sBRGsP": "9",
      "sjzCfH": "Creditmoja"
    },
    {
      "DUkSAIO": "com.prestamo.en.linea.chunlong",
      "ZOaSHz": "2023-10-16 11:49:45",
      "dDFfR": "1.0.1",
      "eGgOeO": "2023-10-16 11:49:45",
      "sBRGsP": "101",
      "sjzCfH": "Préstamo en línea"
    },
    {
      "DUkSAIO": "flypesa.uganda",
      "ZOaSHz": "2023-11-01 10:55:49",
      "dDFfR": "5.0.0822.re",
      "eGgOeO": "2023-11-01 10:55:49",
      "sBRGsP": "50822",
      "sjzCfH": "FlyPesa"
    },
    {
      "DUkSAIO": "com.ss.android.lark",
      "ZOaSHz": "2022-08-06 12:56:30",
      "dDFfR": "6.9.6",
      "eGgOeO": "2023-07-18 14:24:01",
      "sBRGsP": "6090650",
      "sjzCfH": "飞书"
    },
    {
      "DUkSAIO": "com.mexico.loan.manage",
      "ZOaSHz": "2023-04-04 12:27:49",
      "dDFfR": "1.0.0",
      "eGgOeO": "2023-04-04 18:17:09",
      "sBRGsP": "1",
      "sjzCfH": "催收助手"
    },
    {
      "DUkSAIO": "care.finance",
      "ZOaSHz": "2023-10-31 09:36:21",
      "dDFfR": "1.1.7",
      "eGgOeO": "2023-10-31 09:36:21",
      "sBRGsP": "117",
      "sjzCfH": "Care Finance"
    },
    {
      "DUkSAIO": "com.oxxo.digital.contigo.nubank.novante",
      "ZOaSHz": "2022-07-14 18:01:41",
      "dDFfR": "1.0.0",
      "eGgOeO": "2022-07-14 18:01:41",
      "sBRGsP": "1",
      "sjzCfH": "Novante"
    },
    {
      "DUkSAIO": "com.fintech.mykes",
      "ZOaSHz": "2022-07-19 21:33:08",
      "dDFfR": "1.1.7",
      "eGgOeO": "2022-07-19 21:33:08",
      "sBRGsP": "10107",
      "sjzCfH": "MyKeS"
    },
    {
      "DUkSAIO": "com.ahorrar.dinero.chancheuklung",
      "ZOaSHz": "2023-07-20 17:09:39",
      "dDFfR": "1.1.0",
      "eGgOeO": "2023-07-20 17:09:39",
      "sBRGsP": "110",
      "sjzCfH": "Ahorrar dinero"
    },
    {
      "DUkSAIO": "vStudio.Android.Camera360",
      "ZOaSHz": "2018-08-08 00:01:00",
      "dDFfR": "9.9.35",
      "eGgOeO": "2023-07-24 09:34:12",
      "sBRGsP": "212099352",
      "sjzCfH": "Camera360"
    },
    {
      "DUkSAIO": "com.github.kr328.clash.foss",
      "ZOaSHz": "2022-10-09 12:10:27",
      "dDFfR": "2.5.11.foss",
      "eGgOeO": "2022-10-09 12:10:27",
      "sBRGsP": "205011",
      "sjzCfH": "Clash for Android"
    },
    {
      "DUkSAIO": "com.guoshi.httpcanary",
      "ZOaSHz": "2023-02-24 11:55:22",
      "dDFfR": "9.9.9.9",
      "eGgOeO": "2023-02-24 11:55:22",
      "sBRGsP": "999999",
      "sjzCfH": "HttpCanary"
    },
    {
      "DUkSAIO": "com.taobao.idlefish",
      "ZOaSHz": "2023-07-18 10:34:24",
      "dDFfR": "7.12.70",
      "eGgOeO": "2023-10-07 09:48:30",
      "sBRGsP": "347",
      "sjzCfH": "闲鱼"
    },
    {
      "DUkSAIO": "com.booking",
      "ZOaSHz": "2018-08-08 00:01:00",
      "dDFfR": "38.3.0.1",
      "eGgOeO": "2023-07-18 14:24:58",
      "sBRGsP": "901398",
      "sjzCfH": "Booking.com缤客"
    },
    {
      "DUkSAIO": "com.example.demohtt",
      "ZOaSHz": "2020-08-30 09:34:00",
      "dDFfR": "1.0",
      "eGgOeO": "2020-08-30 09:34:00",
      "sBRGsP": "1",
      "sjzCfH": "DemoHtt"
    },
    {
      "DUkSAIO": "com.example.myapplication",
      "ZOaSHz": "2023-10-30 14:55:34",
      "dDFfR": "1.0",
      "eGgOeO": "2023-10-30 14:55:34",
      "sBRGsP": "1",
      "sjzCfH": "My Application"
    },
    {
      "DUkSAIO": "com.loan.cash.credit.prestamos.personale.solyacash",
      "ZOaSHz": "2020-08-30 09:32:16",
      "dDFfR": "1.1.1",
      "eGgOeO": "2020-08-30 09:32:16",
      "sBRGsP": "108",
      "sjzCfH": "SolyaCash"
    },
    {
      "DUkSAIO": "mx.com.tala",
      "ZOaSHz": "2022-10-09 12:14:22",
      "dDFfR": "7.123.0",
      "eGgOeO": "2022-10-09 12:14:22",
      "sBRGsP": "32300",
      "sjzCfH": "TALA"
    },
    {
      "DUkSAIO": "com.loan.cash.credit.branch.tala.fast.lending.mexico",
      "ZOaSHz": "2022-07-19 12:45:40",
      "dDFfR": "2.3.8",
      "eGgOeO": "2022-07-19 12:45:40",
      "sBRGsP": "254",
      "sjzCfH": "OKrédito"
    },
    {
      "DUkSAIO": "com.sipdroid.nxcloud",
      "ZOaSHz": "2023-04-10 09:37:29",
      "dDFfR": "0.3.185",
      "eGgOeO": "2023-04-10 09:37:29",
      "sBRGsP": "185",
      "sjzCfH": "NXphone"
    },
    {
      "DUkSAIO": "ke.co.absa.digitalwallet",
      "ZOaSHz": "2022-07-19 22:08:50",
      "dDFfR": "1.0.11",
      "eGgOeO": "2022-07-19 22:08:50",
      "sBRGsP": "69",
      "sjzCfH": "Timiza"
    },
    {
      "DUkSAIO": "com.mexico.loan.open.purse",
      "ZOaSHz": "2020-08-24 15:56:49",
      "dDFfR": "1.1.1",
      "eGgOeO": "2020-08-24 15:56:49",
      "sBRGsP": "111",
      "sjzCfH": "OpenPurse"
    },
    {
      "DUkSAIO": "credit.prestamos.personale.cash.deposito.inmediato",
      "ZOaSHz": "2022-07-18 11:12:26",
      "dDFfR": "1.0.23",
      "eGgOeO": "2022-07-18 11:12:26",
      "sBRGsP": "23",
      "sjzCfH": "Rapidayuda"
    }
  ],
  "bank": {
    "idCard": "1400104010"
  },
  "base": {
    "birthday": "1994-05-01",
    "education": "3",
    "email": "Reff@gmail.com",
    "lastName": "Rdff",
    "firstName": "Dfgg",
    "middleName": "Gghh",
    "maritalStatus": "1",
    "placeAddress": "Ffvjj",
    "placeProvince": "21",
    "placeCity": "2104",
    "sex": "1",
    "uname": "Dfgg Gghh Rdff",
    "otherLoans": "1",
    "instancyContacts": [
      {
        "contactName": "Tansang01",
        "contactRealName": "Tansang01",
        "contactPhone": "661140121",
        "contactRelation": "0"
      },
      {
        "contactName": "Tansang02",
        "contactRealName": "Tansang02",
        "contactPhone": "604014012",
        "contactRelation": "4"
      }
    ]
  },
  "work": {
    "income": "4",
    "payDay": "1",
    "post": "1"
  },
  "payoutPaymentConfig": {
    "ewalletConfig": {
      "accountHolder": "Dfgg Gghh Rdff",
      "accountNo": "670010401"
    },
    "paymentChildKey": {
      "label": "ewallet",
      "value": "ewallet"
    },
    "paymentTypeKey": {
      "label": "ewallet",
      "value": "ewallet"
    }
  },
  "attach": [
    {
      "channel": "app",
      "newName": "1698905199020107.jpeg",
      "newPathName": "file-upload/1698905199020107.jpeg",
      "originalAttachName": "TzaImg-1698905193057.jpg",
      "path": "file-upload/",
      "purpose": "sfzzm"
    },
    {
      "channel": "app",
      "newName": "1698905209167367.jpeg",
      "newPathName": "file-upload/1698905209167367.jpeg",
      "originalAttachName": "TzaImg-1698905204659.jpg",
      "path": "file-upload/",
      "purpose": "sfzfm"
    }
  ],
  "configPayout": True,
  "applyLoanAmount": 1000,
  "merchantNo": "03",
  "orgNo": "TZA",
  "productNo": "TZA_03_1_20230404052027"
})
headers = {
  'token': '1639424a7a8ebca4aa05a1f985a4569a',
  'lang': 'zh',
  'app-version': '1',
  'app-name': 'PesaPole',
  'channel': 'googlePlay',
  'commercialid': '01',
  'organizationid': 'DCTZA',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
