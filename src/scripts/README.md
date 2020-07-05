## Instrucciones de uso

### conect_to_ibm

Esta es la clase que nos permite conectarnos con la base de datos de IBM. En esta clase podemos encontrar tres métodos:

**get_bucket_contents** --> Donde podemos listar todos los elementos dentro de nuestro Bucket dentro de IBM Watson. No requiere pasarle ningun parámetro

**get_item** --> Donde podemos obtener un elemento dentro del bucket para su posterior uso. Para usarlo solamente se requiere un parámetro "item_name", donde se indica el nombre del item dentro del bucket

**put_item** --> Donde podemos enviar un elemento desde nuestro local al bucket de IBM Watson. Para usarlo, se requieren 3 parámetros.
  - item: donde almacenamos lo que queremos enviar
  - nombre_fichero: donde determinamos el nombre del fichero
  - is_csv: en el caso de que queramos exportarlo como DataFrame de pandas a csv, poner 1 en esta variable
  

### Predictors

Esta es la clase que nos permite lanzar las predicciones ya entrenadas en IBM Watson. En el propio constructor llamamos a la clase conect_to_ibm para obtener automáticamente los datos de los predictores de IBM Watson. En esta clase podemos encontrar ocho métodos:

**predict_cluster** --> Donde podemos, a partir de los datos de la analitica, detectar en qué cluster se encuentra un paciente. Hay que pasarle una variable, llamada data, con el siguiente aspecto:

<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>leucocitos</th>      <th>hematies</th>      <th>hemoglobina</th>      <th>hematocrito</th>      <th>plaquetas</th>      <th>neutrofilos</th>      <th>linfocitos</th>      <th>monocitos</th>      <th>eosinófilos</th>      <th>actividad_de_protrombina</th>      <th>inr</th>      <th>fibrinogeno_derivado</th>      <th>tiempo_de_cefalina</th>      <th>ferritina</th>      <th>d_dímero</th>      <th>glucosa_en_suero</th>      <th>creatinina_en_suero</th>      <th>filtrado_glomerular(ckd-epi)</th>      <th>sodio_en_suero</th>      <th>potasio_en_suero</th>      <th>cloro_en_suero</th>      <th>asat/got</th>      <th>alat/gpt</th>      <th>ggt</th>      <th>proteína_c_reactiva</th>      <th>procalcitonina</th>      <th>interleuquina-6</th>      <th>interleuqiona-1</th>      <th>proteinas_totales_en_suero</th>      <th>nt-probnp</th>      <th>ph_sangre_arterial</th>      <th>pco2_sangre_arterial</th>      <th>lactato</th>      <th>bicarbonato_sangre_arterial</th>      <th>bicarbonato_std_sangre_arterial</th>      <th>exceso_de_bases_standard</th>      <th>calcio_ionizado</th>      <th>calcio_ionizado_corregido_ph_7.40</th>      <th>anion_gap</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>8.09</td>      <td>4.97</td>      <td>16.42</td>      <td>45.09</td>      <td>315.04</td>      <td>54.94</td>      <td>23.81</td>      <td>5.96</td>      <td>0.67</td>      <td>77.57</td>      <td>0.85</td>      <td>278.26</td>      <td>98.32</td>      <td>3365.63</td>      <td>333.71</td>      <td>75.63</td>      <td>0.76</td>      <td>882.38</td>      <td>142.63</td>      <td>4.32</td>      <td>99.66</td>      <td>5.01</td>      <td>7.64</td>      <td>26.44</td>      <td>20.38</td>      <td>0.31</td>      <td>3.54</td>      <td>23.26</td>      <td>7.69</td>      <td>73.93</td>      <td>7.41</td>      <td>44.4</td>      <td>0.76</td>      <td>24.61</td>      <td>25.05</td>      <td>1.23</td>      <td>1.19</td>      <td>1.28</td>      <td>12.55</td>    </tr>  </tbody></table>

La variable data debe de ser un vector o un DataFrame, con el aspecto que se muestra y el orden que se indica.

Este método nos devolverá una de las siguientes opciones:

<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>Etiqueta</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>Inflamación Intensa</td>    </tr>    <tr>      <th>1</th>      <td>Inflamación Intensa con SobreInfección</td>    </tr>    <tr>      <th>2</th>      <td>Inflamación Intensa con Transtorno de la Coagu...</td>    </tr>    <tr>      <th>3</th>      <td>Inflamación Moderada con SobreInfección</td>    </tr>    <tr>      <th>4</th>      <td>Inflamación Moderada</td>    </tr>    <tr>      <th>5</th>      <td>Inflamación Moderada con Transtorno de la Coag...</td>    </tr>    <tr>      <th>6</th>      <td>Inflamación Leve con Transtorno de la Coagulación</td>    </tr>    <tr>      <th>7</th>      <td>Inflamación Leve con SobreInfección</td>    </tr>    <tr>      <th>8</th>      <td>Inflamación Leve</td>    </tr>  </tbody></table>
      
**predict_proba_cluster** --> Donde nos devuelve la probabilidad de cada uno de las etiquetas por la cual se ha entrenado el sistema. Requiere el mismo parámetro data que requiere el método predict_cluster, devolviéndonos un array con el siguiente orden:

<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>Label</th>      <th>Value</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>Inflamación Intensa</td>      <td>0.813184</td>    </tr>    <tr>      <th>1</th>      <td>Inflamación Intensa con SobreInfección</td>      <td>0.036934</td>    </tr>    <tr>      <th>2</th>      <td>Inflamación Intensa con Transtorno de la Coagulación</td>      <td>0.014777</td>    </tr>    <tr>      <th>3</th>      <td>Inflamación Moderada con SobreInfección</td>      <td>0.015259</td>    </tr>    <tr>      <th>4</th>      <td>Inflamación Moderada</td>      <td>0.001546</td>    </tr>    <tr>      <th>5</th>      <td>Inflamación Moderada con Transtorno de la Coagulación</td>      <td>0.000703</td>    </tr>    <tr>      <th>6</th>      <td>Inflamación Leve con Transtorno de la Coagulación</td>      <td>0.105914</td>    </tr>    <tr>      <th>7</th>      <td>Inflamación Leve con SobreInfección</td>      <td>0.008835</td>    </tr>    <tr>      <th>8</th>      <td>Inflamación Leve</td>      <td>0.002848</td>    </tr>  </tbody></table>
       
**predict_home_hospital** --> Donde nos devuelve si un paciente al llegar a la consulta se le debe de dar o no de alta. Para el uso de este método se requiere de un parámetro llamado data, que debe de tener la siguiente forma:

<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>sexo</th>      <th>edad</th>      <th>hta</th>      <th>acv</th>      <th>obesidad</th>      <th>dias_de_evolución</th>      <th>fiebre</th>      <th>tos</th>      <th>disnea_en_reposo</th>      <th>disnea_con_esfuerzos</th>      <th>dolor_torácico</th>      <th>odinofagia</th>      <th>anosmia</th>      <th>cefalea</th>      <th>rinorrea</th>      <th>vomitos</th>      <th>diarrea</th>      <th>peso</th>      <th>relleno_capilar_patologica</th>      <th>relleno_capilar_no_patologica</th>      <th>frecuencia_cardiaca</th>      <th>tensión_arterial_d</th>      <th>tensión_arterial_s</th>      <th>frecuencia_respiratoria</th>      <th>saturación</th>      <th>trabajo_respiratorio</th>      <th>auscultacion_pulmonar_no_patologica</th>      <th>auscultacion_pulmonar_patologica</th>      <th>lesiones_cutaneas</th>      <th>ant_per</th>      <th>rx_tx</th>      <th>rx_tx_pos</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>1</td>      <td>28</td>      <td>0</td>      <td>1</td>      <td>0</td>      <td>27</td>      <td>41</td>      <td>0</td>      <td>1</td>      <td>0</td>      <td>1</td>      <td>1</td>      <td>0</td>      <td>0</td>      <td>0</td>      <td>0</td>      <td>0</td>      <td>88</td>      <td>0</td>      <td>1</td>      <td>94</td>      <td>97</td>      <td>140</td>      <td>246</td>      <td>96</td>      <td>1</td>      <td>0</td>      <td>1</td>      <td>1</td>      <td>0</td>      <td>0</td>      <td>0</td>    </tr>  </tbody></table>

Pudiendo introducir los valores como un vector o como un DataFrame, pero siempre con el orden indicado en la tabla.

Este método no devolverá una de las siguientes opciones:

<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>Etiqueta</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>Alta en Domicilio</td>    </tr>    <tr>      <th>1</th>      <td>Alta en Domicilio - Revisión en 48 horas</td>    </tr>    <tr>      <th>2</th>      <td>Ingreso Hospitalario</td>    </tr>  </tbody></table>
       
**predict_proba_home_hospital** --> Donde nos devuelve la probabilidad de que un paciente se le deba dar de alta en su domicio o ingresarlo en planta. Se requiere el mismo parámetro data usado en el método predict_home_hospital. Este método nos devolverá un array donde se valoran las siguientes opciones: 

<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>Label</th>      <th>Value</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>Alta en Domicilio</td>      <td>0.924329</td>    </tr>    <tr>      <th>1</th>      <td>Alta en Domicilio - Revisión en 48 horas</td>      <td>0.058671</td>    </tr>    <tr>      <th>2</th>      <td>Ingreso Hospitalario</td>      <td>0.017000</td>    </tr>  </tbody></table>

**predict_again_hospital_predictor** --> Donde nos devuelve si un paciente, al darle de alta para que regrese a su casa, volverá a recaer por la enfermedad o se quedará en su casa. Este método requiere el uso de un parámetro data, con la siguiente forma:

<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>sexo</th>      <th>edad</th>      <th>hta</th>      <th>acv</th>      <th>obesidad</th>      <th>dias_de_evolución</th>      <th>fiebre</th>      <th>tos</th>      <th>disnea_en_reposo</th>      <th>disnea_con_esfuerzos</th>      <th>dolor_torácico</th>      <th>odinofagia</th>      <th>anosmia</th>      <th>cefalea</th>      <th>rinorrea</th>      <th>vomitos</th>      <th>diarrea</th>      <th>peso</th>      <th>relleno_capilar_patologica</th>      <th>relleno_capilar_no_patologica</th>      <th>frecuencia_cardiaca</th>      <th>tensión_arterial_d</th>      <th>tensión_arterial_s</th>      <th>frecuencia_respiratoria</th>      <th>saturación</th>      <th>trabajo_respiratorio</th>      <th>auscultacion_pulmonar_no_patologica</th>      <th>auscultacion_pulmonar_patologica</th>      <th>lesiones_cutaneas</th>      <th>ant_per</th>      <th>rx_tx</th>      <th>rx_tx_pos</th>      <th>cluster</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>1</td>      <td>28</td>      <td>0</td>      <td>1</td>      <td>0</td>      <td>27</td>      <td>41</td>      <td>0</td>      <td>1</td>      <td>0</td>      <td>1</td>      <td>1</td>      <td>0</td>      <td>0</td>      <td>0</td>      <td>0</td>      <td>0</td>      <td>88</td>      <td>0</td>      <td>1</td>      <td>94</td>      <td>97</td>      <td>140</td>      <td>246</td>      <td>96</td>      <td>1</td>      <td>0</td>      <td>1</td>      <td>1</td>      <td>0</td>      <td>0</td>      <td>0</td>      <td>0</td>    </tr>  </tbody></table>

Pudiendo enviar los valores como un DataFrame o como un vector, pero siempre en el mismo orden.

Este método nos devolverá una de las siguientes opciones:

<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>Etiqueta</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>Recae</td>    </tr>    <tr>      <th>1</th>      <td>No Recae</td>    </tr>  </tbody></table>

**predict_proba_again_hospital_predictor** --> Donde nos devuelve la probabilidad de que el paciente vuelva a recaer de la enfermedad o se quedará en casa definitivamente. Para el uso de este método se requiere el mismo parámetro dada definido en el método predict_again_hospital_predictor. Este método nos devolverá las probabilidades de:

<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>Label</th>      <th>Value</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>Recae</td>      <td>0.501343</td>    </tr>    <tr>      <th>1</th>      <td>No Recae</td>      <td>0.498657</td>    </tr>  </tbody></table>

**predict_death_predictor** --> Donde nos devuelve si un paciente, al ingresarlo en planta, fallecerá o no debido a la enfermedad. Para el uso de este método es necesario el uso del parámetro data, con el siguiente aspecto:

<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>sexo</th>      <th>edad</th>      <th>hta</th>      <th>acv</th>      <th>obesidad</th>      <th>dias_de_evolución</th>      <th>fiebre</th>      <th>tos</th>      <th>disnea_en_reposo</th>      <th>disnea_con_esfuerzos</th>      <th>dolor_torácico</th>      <th>odinofagia</th>      <th>anosmia</th>      <th>cefalea</th>      <th>rinorrea</th>      <th>vomitos</th>      <th>diarrea</th>      <th>peso</th>      <th>relleno_capilar_patologica</th>      <th>relleno_capilar_no_patologica</th>      <th>frecuencia_cardiaca</th>      <th>tensión_arterial_d</th>      <th>tensión_arterial_s</th>      <th>frecuencia_respiratoria</th>      <th>saturación</th>      <th>trabajo_respiratorio</th>      <th>auscultacion_pulmonar_no_patologica</th>      <th>auscultacion_pulmonar_patologica</th>      <th>lesiones_cutaneas</th>      <th>ant_per</th>      <th>rx_tx</th>      <th>rx_tx_pos</th>      <th>cluster</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>0</td>      <td>69</td>      <td>0</td>      <td>1</td>      <td>1</td>      <td>26</td>      <td>35</td>      <td>1</td>      <td>0</td>      <td>1</td>      <td>1</td>      <td>0</td>      <td>1</td>      <td>0</td>      <td>0</td>      <td>0</td>      <td>1</td>      <td>64</td>      <td>1</td>      <td>0</td>      <td>94</td>      <td>82</td>      <td>135</td>      <td>92</td>      <td>99</td>      <td>1</td>      <td>0</td>      <td>0</td>      <td>1</td>      <td>1</td>      <td>1</td>      <td>1</td>      <td>0</td>    </tr>  </tbody></table>

Donde se puede introducir la información mediante un vector o un DataFrame, siempre con el mismo orden.

Este método nos devolverá una de las siguientes opciones:

<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>Etiqueta</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>No Fallece</td>    </tr>    <tr>      <th>1</th>      <td>Fallece</td>    </tr>  </tbody></table>

**predict_proba_death_predictor** --> Donde nos devuelve la probabilidad de que un paciente, al ingresarlo en planta, fallezca o no. Nos devolverá un conjunto de probabilidades con el siguiente orden:

<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>Label</th>      <th>Value</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>No Fallece</td>      <td>0.125023</td>    </tr>    <tr>      <th>1</th>      <td>Fallece</td>      <td>0.874977</td>    </tr>  </tbody></table>


