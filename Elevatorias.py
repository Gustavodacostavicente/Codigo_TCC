import pandas as pd
import folium

lat = -26.3051
lon = -48.8461

lat_esp = -26.281443
lon_esp = -48.780236

lat_flo = -26.321827
lon_flo = -48.839080

lat_tel = -26.276199
lon_tel = -48.872563

lat_tim = -26.293086
lon_tim = -48.856226

lat_jor = -26.32773151228314
lon_jor = -48.8691024890012

lat_don = -26.287544
lon_don = -48.840909

latgeral = [-26.321827,
-26.281443,
-26.291816,
-26.268231,
-26.277751,
-26.275012,
-26.30196,
-26.366669,
-26.316921,
-26.271546,
-26.273258,
-26.271383,
-26.268491,
-26.266404,
-26.331859,
-26.287544,
-26.287791,
-26.314281,
-26.280615,
-26.322069,
-26.318729,
-26.292138,
-26.326168,
-26.311898,
-26.276199,
-26.290474,
-26.333728,
-26.339061,
-26.286385,
-26.293086,
-26.273935,
-26.334105,
-26.325178,
-26.283504,
-26.268403,
-26.287375,
-26.166696,
-26.321546,
-26.287084,
-26.26534,
-26.269126,
-26.295623,
-26.290785,
-26.311051,
-26.269467,
-26.266712,
-26.37557,
-26.287206,
-26.267406,
-26.282156,
-26.276944,
-26.323504,
-26.301391,
-26.291331,
-26.330844,
-26.281104,
-26.305645,
-26.273712,
-26.334756,
-26.280614,
-26.271374,
-26.33284,
-26.272495,
-26.300484,
-26.323181,
-26.287128,
-26.280435,
-26.307137,
-26.283052,
-26.352489,
-26.288854,
-26.265701,
-26.325352,
-26.276663,
-26.214443,
-26.284912,
-26.326755,
-26.260151,
-26.280689,
-26.210904,
-26.215266,
-26.326914,
-26.289167,
-26.291421,
-26.290389,
-26.293144,
-26.28447,
-26.342326,
-26.198743,
-26.326978,
-26.271011,
-26.279267,
-26.265927,
-26.214407,
-26.322908,
-26.287381,
-26.265714,
-26.346883,
-26.304259,
-26.293707,
-26.281598,
-26.328287,
-26.26687,
-26.323397,
-26.326943,
-26.288328,
-26.289957,
-26.290668,
-26.268233,
-26.270638,
-26.287115,
-26.289013,
-26.281178,
-26.271405,
-26.261994,
-26.26086,
-26.34701,
-26.346915,
-26.285076,
-26.323136]


longeral = [-48.83908,
-48.780236,
-48.879287,
-48.865353,
-48.85448,
-48.863386,
-48.766358,
-48.842372,
-48.815981,
-48.876122,
-48.881563,
-48.847619,
-48.867693,
-48.886478,
-48.79269,
-48.840909,
-48.780661,
-48.862323,
-48.787289,
-48.853677,
-48.803803,
-48.843164,
-48.795037,
-48.84887,
-48.872563,
-48.872502,
-48.788984,
-48.874526,
-48.881808,
-48.856226,
-48.880389,
-48.855276,
-48.803083,
-48.875795,
-48.86585,
-48.776614,
-48.901647,
-48.867343,
-48.883095,
-48.873287,
-48.881619,
-48.867074,
-48.867981,
-48.764696,
-48.856988,
-48.887157,
-48.829787,
-48.864141,
-48.877033,
-48.784201,
-48.885272,
-48.870594,
-48.763713,
-48.866242,
-48.866309,
-48.883016,
-48.864483,
-48.840138,
-48.871753,
-48.785262,
-48.847512,
-48.86785,
-48.88053,
-48.870935,
-48.874711,
-48.842741,
-48.786038,
-48.859721,
-48.878485,
-48.851674,
-48.871209,
-48.847558,
-48.856311,
-48.833169,
-48.814512,
-48.783449,
-48.860618,
-48.839871,
-48.868497,
-48.836541,
-48.896187,
-48.863015,
-48.839045,
-48.776922,
-48.863486,
-48.881344,
-48.787974,
-48.857071,
-48.910536,
-48.854427,
-48.849087,
-48.867999,
-48.868312,
-48.814443,
-48.873419,
-48.844852,
-48.864747,
-48.790101,
-48.869662,
-48.873428,
-48.83806,
-48.873681,
-48.847486,
-48.798278,
-48.872561,
-48.771918,
-48.773034,
-48.867937,
-48.871503,
-48.85759,
-48.896641,
-48.862789,
-48.871097,
-48.85809,
-48.841248,
-48.840206,
-48.790317,
-48.7901,
-48.792537,
-48.813241]


 
map = folium.Map(location=[lat, lon], zoom_start=100)
                           
Raio = 1000
                           
folium.Marker([lat_esp, lon_esp]).add_to(map)
folium.Circle([lat_esp, lon_esp], radius=Raio, popup="The Waterfront", color="red", fill=True).add_to(map)
                           
folium.Marker([lat_flo, lon_flo]).add_to(map)
folium.Circle([lat_flo, lon_flo], radius=Raio, popup="The Waterfront", color="blue", fill=True).add_to(map)

folium.Marker([lat_tel, lon_tel]).add_to(map)
folium.Circle([lat_tel, lon_tel], radius=Raio, popup="The Waterfront", color="green", fill=True).add_to(map)

folium.Marker([lat_tim, lon_tim]).add_to(map)
folium.Circle([lat_tim, lon_tim], radius=Raio, popup="The Waterfront", color="black", fill=True).add_to(map)

folium.Marker([lat_jor, lon_jor]).add_to(map)
folium.Circle([lat_jor, lon_jor], radius=Raio, popup="The Waterfront", color="gray", fill=True).add_to(map)

folium.Marker([lat_don, lon_don]).add_to(map)
folium.Circle([lat_don, lon_don], radius=Raio, popup="The Waterfront", color="orange", fill=True).add_to(map)

for i in range(1,120):
    folium.Marker([latgeral[i], longeral[i]]).add_to(map)

map    