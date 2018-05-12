
import matplotlib.pyplot as plt
import pandas as pd

# years = [1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995,
#          2000, 2005, 2010, 2015]
#
# pops = [2.5, 2.7, 3.0, 3.3, 3.6, 4.0, 4.4, 4.8, 5.3, 5.7, 6.1, 6.5, 6.9, 7.3]
#
# deaths = [1.2, 1.7, 1.8, 2.2, 2.5,
#           2.7, 2.9, 3, 3.1, 3.3, 3.5,3.8, 4.0, 4.3]
#
# # plt.plot(years, pops,  '--',color=(255/255, 100/255, 100/255))
# # plt.plot(years, deaths, color=(.6, .6, 1))
# #
# # plt.ylabel("Population in billions")
# # plt.xlabel("Population growth by year")
# # plt.title("Population Growth")
# # plt.show()
#
# lines = plt.plot(years, pops, years, deaths)
# plt.grid(True)
#
# plt.setp(lines, color=(1, .4, .4), marker="o")
# plt.show()



# Graph of how many people work in professions

# labels = 'Python', 'C++', 'Ruby', 'Java', 'PHP', 'Perl'
# sizes = [33, 52, 12, 17, 62, 48]
# seperated=(.11,0,0,0,0,0)
#
# plt.pie(sizes, labels=labels, autopct='%1.1f%%', explode=seperated)
# plt.axis('equal')
# plt.show()

data = [{
    'name': 'Nick',
    'jan_ir': 124,
    'feb_ir': 100,
    'march_ir': 165
    },
    {
    'name': 'Panda',
    'jan_ir': 112,
    'feb_ir': 143,
    'march_ir': 3
    },
    {
        'name': 'Panda',
        'jan_ir': 112,
        'feb_ir': 143,
        'march_ir': 3}
]

raw_data = {'names': ['Nick', 'Pandas', 'S', 'Ari', 'Valos'],
            'jan_ir': [143, 122, 101, 106, 365],
            'feb_ir': [122, 132, 144, 98, 62],
            'march_ir': [65, 88, 12, 32, 65]}



df = pd.DataFrame(raw_data, columns=['names', 'jan_ir', 'feb_ir', 'march_ir'])

df['total_ir'] = df['jan_ir'] + df['feb_ir'] + df ['march_ir']

print(df)