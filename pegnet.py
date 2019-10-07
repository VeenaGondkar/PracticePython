
currency = ["pUSD",
"pBNB",
"pBRL",
"pCAD",
"pCHF",
"pCNY",
"pDASH",
"pDCR",
"pETH",
"pEUR",
"pGBP",
"pHKD",
"pINR",
"pJPY",
"pKRW",
"pLTC",
"pMXN",
"pPHP",
"pRVN",
"pSGD",
"pXAG",
"pXAU",
"pXBC",
"pXBT",
"pXLM",
"pXMR",
"pZEC"]


# for i in currency:
#     for j in currency:
#         print(f"pegnetd newcvt EC1xKrKzid7xam9nE4snQNtjXeftXnuApr1mhakqWjHBhGzzZ22m FA3rfZFZaktHVYZ9ASwBfdTHYLjNH91vpiTVhT2J6MMy23zekSow {i} 0.00001 {j} -s http://192.168.1.157:8088/v2")



for i in currency:
    print(f"pegnetd newtx EC1xKrKzid7xam9nE4snQNtjXeftXnuApr1mhakqWjHBhGzzZ22m FA3rfZFZaktHVYZ9ASwBfdTHYLjNH91vpiTVhT2J6MMy23zekSow {i} 0.0001 FA39xfwS24WJJqdByQL4nYwsuFgJPNYvUzDf3qNHjQYH7UD9iFvT  -s http://192.168.1.157:8088/v2")
