import pandas as pd

df = pd.read_csv('GoogleApps.csv')

# # Скільки коштує (Price) найдешевший платний додаток (Type == 'Paid)?
paid_apps = df[(df['Type']=='Paid') & () ]
print(paid_apps['Price'].min())

# # Чому дорівнює медіанна (median) кількість установок (Installs)
# # додатків із категорії (Category) "ART_AND_DESIGN"?
# art = df[df['Category'] == 'ART_AND_DESIGN']
# print(round(art['Installs'].median()))

# # На скільки максимальна кількість відгуків (Reviews) для безкоштовних програм (Type == 'Free')
# # більше максимальної кількості відгуків для платних програм (Type == 'Paid')?
# paid_apps = df[df['Type']=='Paid']
# free_apps = df[df['Type']=='Free']

# max_paid = paid_apps['Reviews'].max()
# max_free = free_apps['Reviews'].max()
# print(max_free - max_paid)

# # print(df[df['Type'] == 'Paid']['Reviews'].max() - df[df['Type'] == 'Free']['Reviews'].max())

# # Який мінімальний розмір (Size) програми для тинейджерів (Content Rating == 'Teen')
# teen = df[df['Content Rating']=='Teen']
# print("Min teen:", teen['Size'].min())

# # *До якої категорії (Category) відноситься додаток із найбільшою кількістю відгуків (Reviews)?
# print(df[df['Reviews'] == df['Reviews'].max()])

# # *Який середній (mean) рейтинг (Rating) додатків вартістю (Price) понад 20 доларів
# # з кількістю установок (Installs) понад 10000?

# # 3 рівень
# # 1 Скільки всього програм з категорією ('Category') 'BUSINESS'?

# business = df[df['Category']=="BUSINESS"]
# print("Кількість додатків в категоірї BUSINESS", len(business))

# print(df['Category'].value_counts())

# # 2 Чому дорівнює співвідношення кількості додатків для підлітків ('Teen') і для дітей старше 10 ('Everyone 10+')?
# # Відповідь запиши з точністю до сотих.
# cat = df['Content Rating'].value_counts()
# print(cat)
# 3.1 Чому дорівнює середній рейтинг ('Rating') платних ('Paid') додатків?
# Відповідь запиши з точністю до сотих.

avg_rating = df.groupby(by="Type")['Rating'].mean()
print(round(avg_rating, 2))

# 3.2 На скільки середній рейтинг ('Rating') безкоштовних ('Free') додатків менший за середній рейтинг платних ('Paid')?
# Відповідь запиши з точністю до сотих.
print(avg_rating['Paid'] - avg_rating['Free'])

# 4 Чому дорівнює мінімальний та максимальний розмір ('Size') додатків у категорії ('Category') 'COMICS'?
# Запиши відповіді з точністю до сотих.

# Бонус 1. Скільки додатків з рейтингом ('Rating') більше 4.5 у категорії ('Category') 'FINANCE'?

# Бонус 2. Чому дорівнює співвідношення безкоштовних ('Free') і платних ('Paid') ігор з рейтингом ('Rating') більше 4.9?


