## Instrucciones de uso

### conect_to_ibm

Esta es la clase que nos permite conectarnos con la base de datos de IBM. En esta clase podemos encontrar tres métodos:

get_bucket_contents --> Donde podemos listar todos los elementos dentro de nuestro Bucket dentro de IBM Watson. No requiere pasarle ningun parámetro

get_item --> Donde podemos obtener un elemento dentro del bucket para su posterior uso. Para usarlo solamente se requiere un parámetro "item_name", donde se indica el nombre del item dentro del bucket

put_item --> Donde podemos enviar un elemento desde nuestro local al bucket de IBM Watson. Para usarlo, se requieren 3 parámetros.
  - item: donde almacenamos lo que queremos enviar
  - nombre_fichero: donde determinamos el nombre del fichero
  - is_csv: en el caso de que queramos exportarlo como DataFrame de pandas a csv, poner 1 en esta variable
  

### Predictors

Esta es la clase que nos permite lanzar las predicciones ya entrenadas en IBM Watson. En el propio constructor llamamos a la clase conect_to_ibm para obtener automáticamente los datos de los predictores de IBM Watson. En esta clase podemos encontrar ocho métodos:

predict_cluster --> Donde podemos, a partir de los datos de la analitica, detectar en qué cluster se encuentra un paciente. Hay que pasarle una variable, llamada data, con el siguiente aspecto:

<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>leucocitos</th>      <th>hematies</th>      <th>hemoglobina</th>      <th>hematocrito</th>      <th>plaquetas</th>      <th>neutrofilos</th>      <th>linfocitos</th>      <th>monocitos</th>      <th>eosinófilos</th>      <th>actividad_de_protrombina</th>      <th>inr</th>      <th>fibrinogeno_derivado</th>      <th>tiempo_de_cefalina</th>      <th>ferritina</th>      <th>d_dímero</th>      <th>glucosa_en_suero</th>      <th>creatinina_en_suero</th>      <th>filtrado_glomerular(ckd-epi)</th>      <th>sodio_en_suero</th>      <th>potasio_en_suero</th>      <th>cloro_en_suero</th>      <th>asat/got</th>      <th>alat/gpt</th>      <th>ggt</th>      <th>proteína_c_reactiva</th>      <th>procalcitonina</th>      <th>interleuquina-6</th>      <th>interleuqiona-1</th>      <th>proteinas_totales_en_suero</th>      <th>nt-probnp</th>      <th>ph_sangre_arterial</th>      <th>pco2_sangre_arterial</th>      <th>lactato</th>      <th>bicarbonato_sangre_arterial</th>      <th>bicarbonato_std_sangre_arterial</th>      <th>exceso_de_bases_standard</th>      <th>calcio_ionizado</th>      <th>calcio_ionizado_corregido_ph_7.40</th>      <th>anion_gap</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>8.09</td>      <td>4.97</td>      <td>16.42</td>      <td>45.09</td>      <td>315.04</td>      <td>54.94</td>      <td>23.81</td>      <td>5.96</td>      <td>0.67</td>      <td>77.57</td>      <td>0.85</td>      <td>278.26</td>      <td>98.32</td>      <td>3365.63</td>      <td>333.71</td>      <td>75.63</td>      <td>0.76</td>      <td>882.38</td>      <td>142.63</td>      <td>4.32</td>      <td>99.66</td>      <td>5.01</td>      <td>7.64</td>      <td>26.44</td>      <td>20.38</td>      <td>0.31</td>      <td>3.54</td>      <td>23.26</td>      <td>7.69</td>      <td>73.93</td>      <td>7.41</td>      <td>44.4</td>      <td>0.76</td>      <td>24.61</td>      <td>25.05</td>      <td>1.23</td>      <td>1.19</td>      <td>1.28</td>      <td>12.55</td>    </tr>  </tbody></table>

La variable data debe de ser un vector o un DataFrame, con el aspecto que se muestra y el orden que se indica.

Esta variable nos devolverá una de las siguientes opciones:

'Inflamación Intensa', 'Inflamación Intensa con SobreInfección',
       'Inflamación Intensa con Transtorno de la Coagulación',
       'Inflamación Moderada con SobreInfección', 'Inflamación Moderada',
       'Inflamación Moderada con Transtorno de la Coagulación',
       'Inflamación Leve con Transtorno de la Coagulación',
       'Inflamación Leve con SobreInfección', 'Inflamación Leve'
      
predict_proba_cluster --> Donde nos devuelve la probabilidad de cada uno de las etiquetas por la cual se ha entrenado el sistema. Requiere el mismo parámetro data que requiere el método predict_cluster, devolviéndonos un array con el siguiente orden:

'Inflamación Intensa', 'Inflamación Intensa con SobreInfección',
       'Inflamación Intensa con Transtorno de la Coagulación',
       'Inflamación Moderada con SobreInfección', 'Inflamación Moderada',
       'Inflamación Moderada con Transtorno de la Coagulación',
       'Inflamación Leve con Transtorno de la Coagulación',
       'Inflamación Leve con SobreInfección', 'Inflamación Leve'
