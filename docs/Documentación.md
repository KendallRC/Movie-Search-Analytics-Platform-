
## Instituto Tecnológico de Costa Rica

---

## Profesor:

### Gerardo Nereo Campos Araya

---

## Estudiantes:

### Manuel Calero Ríos 2022082503

### Brandon Mora Díaz 2022164409

### Kendall Rodríguez Camacho 2022049438

### Fabían Vargas Cascante 2018160243

---

## Curso:

### Bases de Datos II

---
## Fecha de entrega:

### 24 de mayo del 2024
---

# Componentes implementados

Para el desarrollo y ejecución del proyecto, hace falta tener instaladas ciertas aplicaciones esenciales, a continuación se nombran cuales son junto a sus métodos de instalación:

1.  Docker:
 - Ingresar al siguiente link: [https://www.docker.com/get-started/](https://www.docker.com/get-started/)
- Una vez dentro, seleccionar el dispositivo en el que será utilizado y descargar el .exe. Además de ello deberá de seleccionar la opción de “Get Started” y crear una cuenta para poder hacer uso de Docker. 
<img src="https://lh7-us.googleusercontent.com/0gYbuFbu5FF7hX-GBaM9joDARo9eB3yPY381xqSXeDW5EaqLq6St4zD_Qecfdi9RlgFFGwZAocpw6Hw-LNyqrw9spPwEAMEIrmxZdrDx97zPrnubVZ5_98YV0le8fuBOjMAR7lVHX3kn6Vj7gq4n_RE" width="700" />
- Durante la instalación, debe darle continuar a todo, una vez termine la instalación, Docker iniciará y le desplegará una encuesta, además le pedirá que inicie sesión nuevamente.
- Una vez completados esos pasos, solo hace falta instalar Kubernetes, para ello seleccione la tuerca de arriba a la derecha. Una vez dentro seleccione la opción de la izquierda llamada Kubernetes
<img src="https://lh7-us.googleusercontent.com/4LU4VlvHCxFhivaLPp9y8iI5LKTutENwWYguZGem3byjOMtg-mju8U4ixB4JsokgNcUb8g-6O0m0y9cHyTGwN9Lnp7O4TMX00TVtUhL3d0wqnhpTSXyhP9bZH3zH-tnx2eo53JrZ5KfElcQ2O2uCRLI" width="700" />
- Una vez seleccionado, se debe seleccionar la opción de “Enable Kubernetes” y presionar la opción de abajo a la derecha.
<img src="https://lh7-us.googleusercontent.com/RV6f0wmwpp6mTgqJXr60gW6xYiRh9vItoAf47aFXkHipgQ6Uc8wLb0f7JtVtv9wuWpjLSMzl4BnV4bQrSNINevEOcv_SyVgpf5iDSPyM2crA8AY7n2cyBpyS67MW-EUWGz1nSu73LgTJCAOVtMcobCU" width="700" />
- Una vez seleccionado, toca esperar unos minutos a que finalice la instalación. Una vez finalizada se debe reiniciar el Docker o bien la computadora para que Kubernetes funcione. Para reiniciar Docker, debe presionar el símbolo de apagado ubicado abajo a la izquierda.
<img src="https://lh7-us.googleusercontent.com/DBYgXB0c12fSX8HV_uGxA2tJSbDkUM7QxtY-oBBNzW_Iz52u5qlJLnM1M76F8y0wkRA72413t8v8B66Z8x9wvUX_8LVrfPildTFCM71-kPWJhohUC-8ukdpytWrAV80esgZPk6cYlFYiLcPl_wLBha0" width="700" />

2.  WinRAR:
- Ingresar al siguiente link: [https://www.winrar.es/descargas](https://www.winrar.es/descargas)
- Puede usar el descompresor de archivos de su preferencia, en este caso usaremos WinRAR para el ejemplo. Una vez ingresado al link, debe descargar el archivo que más se adapte a sus necesidades.
<img src="https://lh7-us.googleusercontent.com/Ce8zQmUiTJlzLQzZlHNkBoB8ZhgMgjXnGN2M3WFdObuX7O_zFBX0GwjmltmS555I2wF4FXOK4g7WH3mYuYr75tL0p8-acPSGq0tKDrObiqK2d05I9OIkIh0hzNhNKxXZ7hLxmLDsJ3sxtvMU22WrDtg" width="600" />
- Una vez descargada solo debe de instalarla. Ya con eso tendrá el descompresor de datos listo para ser utilizado.
3. Helm:
- Ingresar al siguiente link: [https://helm.sh/docs/intro/install/](https://helm.sh/docs/intro/install/)
- Una vez dentro, debe bajar y seleccionar “release”
<img src="https://lh7-us.googleusercontent.com/7r5khisSQi14742qwlKBCODvKs9AM8_lutJjQsoyGk_MSvXjlFE7iRXLv7Z8-vk-lhHgXKNdtiStGygzcjNltFwV8ycnvlzcBXlVUBdKdIzKr-gInBkQQjwhUEmCIQ9tm2RU5gzwfJYF5Z08UVk8oZI" width="600" />
- Al entrar, se redirigirá a GitHub, ahí saldrán las versiones de Helm, debe seleccionar la adecuada para su dispositivo.
<img src="https://lh7-us.googleusercontent.com/xlyzA7FcczehOkHCKh76ALaamY3jSy6p7xgoKevtMtQTGnGJxbz2MuJCbPU1gnFzKiEkzwBY2YDRrJUjHTfN6AtcNm-XUK3DPWYGxZXz6urR-REZ3LazTB2hGqFXI9C6pW1X27gn3tI-NtaHj_0_hm4" width="400" />
- Una vez descargado, debe descomprimir el archivo. Una vez hecho debe abrir la carpeta y buscar el archivo helm.exe. Una vez localizado, debe obtener la ruta o ubicación del sitio donde está guardado el helm.exe. La marca amarilla es una guía de dónde estará la dirección del helm.exe.
<img src="https://lh7-us.googleusercontent.com/qA_rSVatETtcbpb4_GaOcBCIniB4TT97DITVY9jkWvCkmGyZ3QL99pfeQTVdNRnzW48QEbEUmb6m4q7a-GNsGYgMjyFVKkJWYER36qMJLDgevHcx8-fO7eUkOdn5UA7BO65siB1bRqO5dbzyexQg3LA" width="700" />
- Ahora, debe buscar el editor de variables del sistema de su dispositivo. Una vez dentro debe buscar el elemento llamado Path e incluir la dirección del sitio donde está almacenado el helm.exe, dicho proceso debe realizarse tanto en el Path de arriba, como el de abajo. Una vez realizado le da en aplicar y aceptar todo. Al realizar esto, tendrá instalado Helm y listo para usar por comandos.
<img src="https://lh7-us.googleusercontent.com/9UwVChpT29UkswhFz3m_zVSmTKZOzrb3j-NbbcdSfOBnmhNAiS612ZapKEIdPkz8BrUQMQAlOF2wY5LnexBt_1M0zBfOjq6izjtFhTsDGB6IPXcHkgEV6CmCFEXFmdFdCgIKUANBeNShm8pfjlCjnYs" width="400" />

<img src="https://lh7-us.googleusercontent.com/QMPvgtzMZxzDDZECO8kuK0RJwKgWW6kxo0ypvUBO0yq2UVdM1S2nn8wmSvh8YeSiagWMp7NC4-1AFYi2uJSnlr3gqTq_DyrNEtCW_YgWZBMFQbeVPkxiNhd4zS2nSBm4ZGsiwev8xibRmVg2j1Chv2A" width="400" />

<img src="https://lh7-us.googleusercontent.com/S1SPQJkPjmxBZIzGiUWWD7rnmq0RiOAjZqeCsj3P6nQuxnM8Sf7Wl-TPG8y6X5ZYRe9EFoSznMqg36ZgtMdMnpFe-7X-YFudagE_RqpPiSqzNZgyXefwTGlFLMPMlIETUW8wFmhpG6HfOUF3TuaWcXs" width="400" />

4.  Lens:
- Ingresar al siguiente link: [https://k8slens.dev/](https://k8slens.dev/)
- Una vez dentro, seleccionar la opción de descargar para su dispositivo
<img src="https://lh7-us.googleusercontent.com/1g98137F1q3NCKBwXPOUMmvMwsyf1GE7GHiKCrAJ7UdMgjuAYiBvisRFpaCv9U1GIYbrFsLtFQzVu-Vx7IJr5FYXFbosGZQ7UdNf9uITN1MzkWdlYNeiDDamWhH0GGeOS96WUeNcIrL36UMwMI7HTDg" width="700" />
- Una vez dentro le va a pedir que inicie sesión, cuando lo hace ya tendría listo para utilizar Lens. No necesita configurar nada, pero si necesita ingresar a otros sitios, pero más adelante se le explicará.
- 
5.  Python:

- Ingresar al siguiente link: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Una vez dentro, le da a descargar la última versión.
<img src="https://lh7-us.googleusercontent.com/iXFNaU_jEwmNprkyxKp5-CvF9AVB70OhhLJWYWbkI9odh2gNVHXjHZEdzXzcwB85iAldS3l-rCnFhHVA3XQgkgofyOUPt_BbjLhEIdYgtHHk1AYrmL1K6ysk8PGIxafSrz_f97sanwe-DpyUaJEpcKg" width="400" />
- Durante el proceso de instalación, solo es importante marcar las siguientes opciones.
<img src="https://lh7-us.googleusercontent.com/avQ_c2N8wT0mr6--ym1x8El5uMFZHwfSDdKJMizmzDpVZ5XD3BZcq9O0XtzgXbfo7oOm84FOlt11_3JHx7u-FwAM2ozClIzQgalaUaTja7GEVsE_N9bLcFswIgQrI6YhSvCMa0h742Bpu3oE9cUQDOQ" width="400" />
- Una vez seleccionadas, continua con el proceso de instalación, dándole continuar hasta que termine la instalación.

6. Thunkable:

- Ingresar al siguiente link: https://thunkable.com/
- Una vez dentro, debe iniciar sesión en donde indica el circulo rojo.

<img src="https://lh7-us.googleusercontent.com/2CTg7WGqpbPABFwN4HuoNpSy8o5D94VacRZpsSEUAGIG5NXCvBU6aDVazFU54iztnRN37jx9zSVnM9p8dMZjbWB4YZbjoaY21gG6qG6uS_dR-0RV1tz3wJjn6i1RK3E9uF2gmARMx3HIsjsZM9Dmlfg" width="400" />

- Con eso se inicia sesión en la página, ahora se ingresa al siguiente link para ingresar a la zona donde se realizan las pruebas vía interfaz gráfica: https://x.thunkable.com/copy/f3a0df8f2d2f7a1f7faf573ace432c57

7. Ngrok: 
- Ingrese al siguiente link: https://ngrok.com/download
- Una vez dentro, seleccione el dispositivo donde desea descargarlo, en este caso será por Windows usando su instalador.
<img  src="https://lh7-us.googleusercontent.com/fPywHELQ21PcKcGP13CqfOJ9V-XDJNabws9_tFzBCynLVtC_4EoJ7-4g_cBCNOCAjKTnZzD2D_4nYjwu4Zti3TNKu4ovZUHNu7_SOMbd5hLMzNvNX1_Q7uo42MPK7BFwVce9jjqa5lvYqgL2V7GExrg"  width="400"  />
- Cuando se descargue, se tendrá un archivo .rar, el cual debe descomprimirse y buscar el archivo con nombre ngrok.exe. Una vez se ubique, debe realizar el mismo proceso que se hizo con helm, pero para evitar complicaciones puede colocar el ngrok.exe en la misma carpeta que helm.exe.

---
# Instrucciones de ejecución
1.  Se debe ingresar al repositorio de GitHub: [https://github.com/BAMDH/2024-01-IC4302](https://github.com/BAMDH/2024-01-IC4302)
2.  Una vez dentro, se debe realizar lo siguiente:
- Seleccionar la opción verde llamada “Code”
<img src="https://lh7-us.googleusercontent.com/oi8ts8Wmb2qYQ1sWNlXoueAFBqMbq3ihgvpNSZ1tnVgU4ucb2cZKCtpZzeMsH-fxA2RcokPZ3ZuRKe1cjoQYGRXhMeAZ9u61_sYCBtZZV3ja_rukMNaG0-Me4noDsq9wBAYdna_lm-8hx_sPTSCsPdw" width="700" />
- Una vez seleccionado, se debe descargar el proyecto en la parte indicada con rojo
<img src="https://lh7-us.googleusercontent.com/L1EAYfM3wmB7co4EjETzDJPuY8wZACZaLDvgI5nFg3HpXiQqwY3SmjBkYG1KCpXhrfKi19w4mi1equTrH2mG3m6ALU20WaQG5N97MDJREKuwutETINXGmAe2z_MxKFzZ-CzU5xKlooNcNrU1Jl7bUrc" width="700" />

- Con esto se descargará el proyecto, el cual debería abrirse con el editor de código de referencia.
3.  Cuando se abre el archivo, selecciona la carpeta P2 y debe aparecer lo siguiente:
<img src="https://lh7-us.googleusercontent.com/UOdI5uiATynxK032fzW4CrIEtN9XIJmURawTUdl1icQZBEn4KLCemz94j-0DmphBDMFf6oahwx59G-y63M9XaGQVXxGnHVduyy5dnSzQV-9XhImj_smVEj2IeYMJKS3u5e1RIhH0OiugqBY91bYjf3w" width="400" />

4.  Se debe seleccionar el archivo llamado run.sh y ejecutar en la línea de comandos lo indicado dentro del archivo, pero antes se debe realiza:
- Primero se debe tener abierto o en ejecución la aplicación de Docker
- Una vez en ejecución, se debe de ingresar en la línea de comandos (cmd) e ingresar a la ubicación de la carpeta P2.
- Cuando se esté dentro de la carpeta, ya se puede ejecutar lo que indica el run.sh
<img src="https://lh7-us.googleusercontent.com/BxmrSsU9UfeBfI-O4dZHv8H3PbRlhnOJPvkGV7YIyqknFaQb0IQuwc_uK6QoMIE8dfIGK04vN8WSacbSXxCcxogohWejFJiTliVt9aFUP6V48OxJhqWIop2IyGD0ni_J8ehm3sKWerOX_AzNgFpaimk" width="300" />

5. Una vez instalados todos los elementos, se debe ingresar a la página de thunkable, cuyo enlace a la interfaz de ejecución se indicó anteriormente.
<img src="https://lh7-us.googleusercontent.com/9DT91-uwU2BJpTZOsXamczMr3h3yD4pOufTbmrwaef0llNMmi4IMtRykz8cpbgPU2gyidj4baJ_RJ11DJ_vT88QVBHCOYANbbUsHGwdflrIjHk41y9ZkmsNTxomQ8X_YF0stRPV2dfHKEZ8Kq7hKhLk" width="700" />
    
6. Ahora debemos dirigirnos al apartado de "Blocks" y seleccionar la opción en circulo rojo, ahí sustituiremos ese link.

<img src="https://lh7-us.googleusercontent.com/vCBrLfmL3VCwVSC_Jw2wk1IPgcoItgdwD8AQvpJrGzHOEmjwMXN2EOfSJP-Sy1wRSvhfmAe4VLTTiRlQz8AgG4vNZ-9qw2mS8M1Fbn9uP6yTXjBc_L4juU2HBP9gATZvPlY_nwDKDHjcQq0GY7qfPPU" width="700" />

7. Dicho link será sustituido por usando ngrok, para ello ejecutamos el comando: ngrok http http://localhost:5000 en la línea de comandos y seleccionamos lo marcado con rojo.

<img  src="https://lh7-us.googleusercontent.com/4xvrSjBxCxbSzwwVT90B_6n-_5wOSvVy971r1K_VOsQ_gPTOFx0fDrqwNVx71_eb2KumTMbu4bGzWPuM938hqCZUhCAl20bf7eY1cVTfOF-fPDJRbdjcJCHJROcLHJuUztQocFzeaQb2sc9MRJ5d0DM"  width="500"  />

8. Una vez copiado dicho link lo sustituimos en la opción antes descrita, recordando que el link debe terminar con .app sin ningún caracter extra:
<img  src="https://lh7-us.googleusercontent.com/hxfxcqyTFT_DNc3lDCnYG4jqsQZcsGi3uv4wSkHLCsArVgca3jrOUQOLFL4Nq-7evTHLuJ10mzCKCFBHqVnDvovJ_B74ivpYQ4Dyn5mAM8AzPz0fbjCGh8jJW1HZgwMqfiSJSXU6OLa1KpveF9aT96U"  width="700"  />

9. Ahora volvemos a "Desing" y ejecutamos la opción de "Preview" para poder interactuar con la interfaz.

<img  src="https://lh7-us.googleusercontent.com/zkcJpj9jEjqG8nQWqyW_SO9Fa5DcAFLoE4tG7pxDj0ctNm0f1G1uE3vPzC5Z_vTHWCAcU7C9nH6rmR4wVgZvzzWN_-5rWn57FFwI4-3UxasiDihvtKIVY-03EjwMPY2LDZYm_1NLJtPqhKpe9m4Gs5c"  width="700"  />

10. Ahora estaremos interactuando con el menú principal, ahí tendremos dos opciones, registrar y login. En caso de tener cuenta, debe unicamente ingresar su email y su contraseña, en caso contrario debe crear un cuenta en la opción de register para poder ingresar.
11. Una vez dentro, se despliega un menú que permite volver al inicio o seleccionar la base de datos que desea consultar.
<img  src="https://lh7-us.googleusercontent.com/YFGXmHDbSnXXIC3OZL6lTDgBLJnW8OpSnZ2W05Ey56Aj5jfYsNTFS76kBKWHKwZjVJPFZESRT478XXtcadvQ3rut0od6g4J8AdE0jFeXqonFsyzAumAn-C5mz2G98ldE7_1UH-FqwS0fgCCztpRYnhg"  width="300"  />
 
12. Cuando seleccione la base de datos a la que desea realizarle una consulta, se le desplegará otro menú, dicho menú contienen opciones en las cuales debe colocar el dato a consulta, como lo es el nombre de la película. En caso de no colocar nada no aparecerá información, por lo que es necesario de hacer. En este ejemplo se filtra la película de Matrix. Cabe resaltar que el nombre de cast y directors deben ser exactos para poder realizar la búsqueda de ellos.
<img  src="https://lh7-us.googleusercontent.com/3VUJm0uRqLZ5aY6a92frFwiAiYjFMVSP__t4gSJq2Edz6H2zlkmzfChQ_KzP-3Ceu5y15DLlnz7_prX3q-7WvhIhxckbx-qujhaGo1dKP0qbF_YxKM-QTbDTHZM-kgrOZta1deeClR-OeU1ZIy1995s"  width="300"  />

13.  Una vez realizado, aparecerán las películas, para poder filtrar por medio de la película, debe precionar sobre el nombre de la misma.
<img  src="https://lh7-us.googleusercontent.com/F71dzoe1A74nORCErq7-o2EBgY-DKgtYhhWSnCXqobr2ft2O_0Xpacd4pTcEdXSm5QMveeDqlLKFEZduAW2qKF7OtZU4qVHPoJjuRT7Vu_XqAhNYmmTkJL2zGBJlRHz2uEKlTVkviOoSqdRNcUZC3_8"  width="300"  />

14. Cuando se selecciona se muestra una nueva interfaz, ahí seleccionaremos a la persona que deseamos filtrar y la opción de filtrar ya sea por actor o director, aclarando que si el switch está azul indica que se busca como actor, mientras que gris busca por director.
<img  src="https://lh7-us.googleusercontent.com/VmrlLygSpvRcbsNjjkAB6gp8wkINrKpM9HdvYhh4FDi1znAnCvyt3aMtRwgIhgK-2PhgsJFkjWWi3Bd9mRcD9GAzVJDfnnxFpKkZFKvRs1x-YTTKWQsEQm2O174okjDMAI2dugqr650dwMmFdi-A0eM"  width="300"  />

15. Cuando se filtra, en este caso a Keanu Reeves como actor, saldrán todas las películas disponibles en la base de datos que cumplan dichos requisitos.
<img  src="https://lh7-us.googleusercontent.com/IqqnvdQ_a7mzEPjT4wPZ_JrGSdEYws4HlPC8zqJpiDl0p1FCzB5cVAvpaEZ6MSBsLcnZZa4jwGuLvzZVvAl0bWhTPa5LX45O7Cgk3KkR9n7TqPTkQvBLBB3_fjgso2dPhRucRll85L4mKXZ4Py0ub6A"  width="300"  />

16. Con esto finalizarían las intrucciones de consulta por medio de esta interfaz, lo mismo aplica para Neo, con la diferencia de que contienen datos distintos.

17.  Ahora solo queda observar el comportamiento del sistema por medio de observabilidad, pero para ello necesitaremos ingresar a Docker por medio de Lens:
- Se debe seleccionar la segunda opción y se desplegarán varios elementos
<img src="https://lh7-us.googleusercontent.com/g_Wcxrssbgh4W4ea-yqDMNeIf2ZZUwwDD9LEBeAJoPDrmisXu5DPJvEmrvz2XNS3CpCy9offf3wTaZ8n8mi1ZGEbeBcDeZMXwyfccT8FWbKr_ICs5uotXuGVPvEggBI0yJTmH3mVaQ_wKRehcW2jGQU" width="700" />
- Ahí se debe seleccionar el llamado “docker-desktop”
<img src="https://lh7-us.googleusercontent.com/fdMwiRB0VE7t6FdE5jBwXVUe25R2jS88S4n4BeUZ1Ws3u-2nf9rhN0cAoNVxZvHab7HNuRkpj1UyjHyr3K3f1fFLzjwGQy1E1Bjiwq3OifKoPsC2iQx7dhdK4fqW91vDFwQo7K10yVfRx0dJmKlSHUA" width="700" />
- Con eso de abrirá el Docker en Lens y se mostrarán diversos de sus elementos, se debe seleccionar el llamado “Workloads”, el cual desplegará una serie de elementos, de los cuales se seleccionará el llamado “Pods”
<img src="https://lh7-us.googleusercontent.com/ejV5n64bA7M_S3O9o_x7NzWLGFADlpiIeAwFbAUrZNe2Cu33IQZoVgF3veV8MhNh-joSqwoWjtz6_G-fMnN2YZEYOsK-7788DPiDRtCFFTr8l4OD6l7b4nhHYy_smKrmJd9O7D48rIDjtUgbtbArdgo" width="300" />

18.  Una vez ingresado en Docker y seleccionada la opción de Pods, se debe buscar el elemento cuyo nombre posea la palabra “grafana”
<img src="https://lh7-us.googleusercontent.com/H7LA9WPPTSraXYrT4bqA_vOYr7x5ApDDQea9i3xInGws9UH2csmz2ElvLe1j04p8bZ-gILKCuDJm6oHpfmAKBGQifio2eCRRXtXxf66Q6AH9o7Z5vsBPJNPa7QQJe6mo_vM67sX_Q_8mXe-VYgWojqA" width="500" />

19.  Una vez seleccionado se mostrará un menú a la derecha, el cual bajaremos hasta hallar la opción de puertos y seleccionar el número que sale en celeste y colocar manualmente el puerto 3000.
<img src="https://lh7-us.googleusercontent.com/nWeAjAZKQMlbyi2kYp3akX2qW153nSX24xUxCmKP5tltJt8GsFVRLxdGy7TxziYBWWR6pHhbNdjVhAGYEemzbguuDod7zPEigvaoGmXgph5qcDYtRcn4lKJ-jLF3fQKd39G6gHk_Vp1RjPxuREWa4hQ" width="600" />

20.  Una vez dentro, se solicita usuario y contraseña, para obtenerlo presione en los ojos que salen en el Pod de Grafana, ahí mostrará el usuario y contraseña que debe ingresar.
<img src="https://lh7-us.googleusercontent.com/hTFybmYTekuX52E-WboR-IJN4bKAu7ckmAsHxiXw4AZAtbPDe7z8-TogIEc6FbAp0n_GYQMe1uB8MD93HKCsRpole36wImEhi0Ye5Oz8dUiXvkR55227l0xiqD9kPUOLnCclgnwozPs9gOvjCLTs6Bs" width="700" />

21.  Al ingresar el usuario y contraseña se desplegará el menú del Grafana, ahora debe ir a la parte de la izquierda y seleccionar “Connections”, ahí dentro debe darle a “Add new connection”. Una vez seleccionado, debe presionar la lupa y buscar “Prometheus”.
<img src="https://lh7-us.googleusercontent.com/3B0_bgupjz9pT9TE8p4-jIxVaXck4A1r4DHMM16GDZDAHwc73fS8P34-FBmx6bcaYv0yjpPahOZah-CEpkjNg1k_8rW8TRDflx_S5S1LBDuYrKgeRdyLHLl0XfnCOI1YFADcBq7x9eretUXSWqNs96I" width="700" />

22.  Una vez seleccionado, hace falta configurarlo, por lo que debe de introducir el puerto de Prometheus y crear la conexión.
<img src="https://lh7-us.googleusercontent.com/XXLKntFTh4SqXiPV9yAG9DlSLzgr-EB8a1yW8FoanBthBTpxgfN8Pqa-ck42aaRDDbTfyytfYcOI8Jy0yZbp9v6qeqowsmgg8N1XIvh0VOz8wSkija_QycIajfwZQUkMMO2rG3l-JsWV1_9iLbjMeYA" width="700" />
<img src="https://lh7-us.googleusercontent.com/mA5WNGN90UxPaU_N7yuVuRh2gvS-9zMkmpTeQOetdF1E-3Gp8o_ze7pGp8LTFO64aR2NFnZMlUJwXLFYVz0nBAIycYFHdOFWlPr9DjpOG-dPKFX21x247Y2bvXoo8G_eR1tTt4veNk7bMyKmmzOW19Q" width="700" />

23.  Una vez configurado, nos iremos a la parte de “Dashboards” en la izquierda y darle a “Create Dashboard”. Ahí dentro debe darle a “Add visualization”.
<img src="https://lh7-us.googleusercontent.com/jcvWFgWp3oK7ZzpT9HtD8YKkEomXzRFKaD_5R5AbGfM-FfXpML_73GmCLNFwQzH1QMlC35jLMIu4iQd3ItvECswH3xs7yAvjrTaV3AKZheCVQpHu9w__ISvq-hFEA4V7J6W0eI7AmCqRhQQZ-Xt2pHI" width="700" />
<img src="https://lh7-us.googleusercontent.com/ewdvTadXiIIJ2GbP-55tMFsnsIGmX3dP-gS6mxSLsmJTs5liZmDIg2rtNPRAYaCdl6BimFAEbhl90evDqRcukIswcAKLLOoQlxfMXBJCH-tJGnmZnGhkG6uO1EmVsM4ZCVKH03xBEva933p6o0bJMVA" width="700" />

24.  Una vez hecho, se despliegan varias opciones, pero de momento nos interesa únicamente Prometheus, por lo que solo seleccionamos esa opción.
<img src="https://lh7-us.googleusercontent.com/MvjpdRPdzYa6Xywsp1uGlTjO4XwesRiG1UZ4l9kqaS8g8-NMuh7wgCo_b3fiYmOktbSYoTj1y0mrsDaUhltrjNqELt_p2Pv0Vx39QWG8UV4yaf2NFiztWZ0phKcfrjgE98lf-ic7J58KS3WE5209aB0" width="700" />

25.  Ahora se despliega un nuevo menú, aquí ya seleccionamos las métricas que deseamos ver, para ello seleccionamos la opción de “Metrics explorer”.
<img src="https://lh7-us.googleusercontent.com/BjMkrutD_qdBEqOCbkiHA0Bg5t_D8b2nCZaVgHDmE1xLdlcCwsVDTTSDNumN6KVyHy9RONNd6q0ODbIInjwwpAUGt5kQEvP_-8SlEveE4XHuDZgdM01AopaLuWk91xfRONZJ1SWcOdHlJKqHB01yHAg" width="700" />

26.  Cuando estemos dentro ya podemos seleccionar entre las muchas gráficas que hay o buscar una en específico, luego sería presionar el “Run queries”.
<img src="https://lh7-us.googleusercontent.com/lbafVQrCDYdNRy6phNaVUULBLqukvSGtaQmOneSP18eHj1DuPBSGFyrQzp7HRcr7QDyrGFSxWEM1P_EBZcRhf4-nwUbOs__ast5Am2vUAKZ6zapFbF3iUFLf0POjv4bJmfy9gELifYHATSkhIy4bYRU" width="700" />

27.  Ya con eso hemos ejecutado todos los procesos disponibles en el proyecto.
---
# Pruebas realizadas con pasos

## Prueba 1

Para esta prueba se hará uso de la misma interfaz de Thunkable para consultar datos. Para ello realizamos:

- Primero iniciamos sesión.
- Una vez dentro seleccionaremos mongo.
<img  src="https://lh7-us.googleusercontent.com/YFGXmHDbSnXXIC3OZL6lTDgBLJnW8OpSnZ2W05Ey56Aj5jfYsNTFS76kBKWHKwZjVJPFZESRT478XXtcadvQ3rut0od6g4J8AdE0jFeXqonFsyzAumAn-C5mz2G98ldE7_1UH-FqwS0fgCCztpRYnhg"  width="300"  />
- Buscaremos una película, en este caso Matrix. 
<img  src="https://lh7-us.googleusercontent.com/3VUJm0uRqLZ5aY6a92frFwiAiYjFMVSP__t4gSJq2Edz6H2zlkmzfChQ_KzP-3Ceu5y15DLlnz7_prX3q-7WvhIhxckbx-qujhaGo1dKP0qbF_YxKM-QTbDTHZM-kgrOZta1deeClR-OeU1ZIy1995s"  width="300"  />
- Con la información que se despliega filtraremos por una película, para ello seleccionamos el nombre de la primera.
<img  src="https://lh7-us.googleusercontent.com/F71dzoe1A74nORCErq7-o2EBgY-DKgtYhhWSnCXqobr2ft2O_0Xpacd4pTcEdXSm5QMveeDqlLKFEZduAW2qKF7OtZU4qVHPoJjuRT7Vu_XqAhNYmmTkJL2zGBJlRHz2uEKlTVkviOoSqdRNcUZC3_8"  width="300"  />
- Aquí dentro, seleccionamos a Keanu Reeves y lo filtramos como actor. 
<img  src="https://lh7-us.googleusercontent.com/VmrlLygSpvRcbsNjjkAB6gp8wkINrKpM9HdvYhh4FDi1znAnCvyt3aMtRwgIhgK-2PhgsJFkjWWi3Bd9mRcD9GAzVJDfnnxFpKkZFKvRs1x-YTTKWQsEQm2O174okjDMAI2dugqr650dwMmFdi-A0eM"  width="300"  />
- Ahora se muestran todas las películas donde él es actor.
<img  src="https://lh7-us.googleusercontent.com/IqqnvdQ_a7mzEPjT4wPZ_JrGSdEYws4HlPC8zqJpiDl0p1FCzB5cVAvpaEZ6MSBsLcnZZa4jwGuLvzZVvAl0bWhTPa5LX45O7Cgk3KkR9n7TqPTkQvBLBB3_fjgso2dPhRucRll85L4mKXZ4Py0ub6A"  width="300"  />

## Prueba 2:
Realizando el mismo proceso anterior, pero haciendo uso de la base de datos de Neo.
- Primero iniciamos sesión.
- Una vez dentro seleccionaremos Neo.
<img  src="https://lh7-us.googleusercontent.com/YFGXmHDbSnXXIC3OZL6lTDgBLJnW8OpSnZ2W05Ey56Aj5jfYsNTFS76kBKWHKwZjVJPFZESRT478XXtcadvQ3rut0od6g4J8AdE0jFeXqonFsyzAumAn-C5mz2G98ldE7_1UH-FqwS0fgCCztpRYnhg"  width="300"  />
- Buscaremos una película, en este caso Matrix. 
<img  src="https://lh7-us.googleusercontent.com/3VUJm0uRqLZ5aY6a92frFwiAiYjFMVSP__t4gSJq2Edz6H2zlkmzfChQ_KzP-3Ceu5y15DLlnz7_prX3q-7WvhIhxckbx-qujhaGo1dKP0qbF_YxKM-QTbDTHZM-kgrOZta1deeClR-OeU1ZIy1995s"  width="300"  />
- Con la información que se despliega filtraremos por una película, para ello seleccionamos el nombre de la primera.
<img  src="https://lh7-us.googleusercontent.com/fHUX0QkevyQYuD7SLzIm722V98wzP0TQtS3Q6qrt43D4NgvZ26FgvNsAR_H6llg2WGscMGTBmILWFRHYJIH1jtLGX9eMWOSnPznPxz6yUMRRZOWq0eO5YdD_2qt0ozD5N2y7f_Pj-xuMkz_8wWGyS-E"  width="300"  />
- Aquí dentro, seleccionamos a Keanu Reeves y lo filtramos como actor.
<img  src="https://lh7-us.googleusercontent.com/MGBt_i7XMjH2df8g5cgh4XTxwm6CM87FY2hsir8ndlOwu2iBpocUPgboim3SDoIdJxNdt49UhMvhcd6-eo4xiAck1qYZssH884X9Vn2wWfqydYhtOoUMpu7n9osw6k1YtLtAgAet2ZzO3VzgbZw9eFk"  width="300"  />
- Ahora se muestran todas las películas donde él es actor.
<img  src="https://lh7-us.googleusercontent.com/53HuA34NlOD1CRHLheWZq9mMWXYd-Cge3Pqguy6hhU6P20OcZCmI5dvUGorq73ojw_OyqxqillmC4-BmdT4CkDA9IrGjIRzHGpWAd_Ox1X8VEdbYY8Pq14_grhPPGkJGH6RMGlD5Q602bS1D9AJXSCA"  width="300"  />

## Prueba 3:

Esta prueba consiste en poner a práctica los diferentes componente de observabilidad. Como primer instancia, ingresamos desde Lens en el pod cuyo nombre contenga la palabra “Prometheus” y seleccionamos su puerto, el método de ingreso a jobs ya se indicó en las instrucciones de ejecución del proyecto.

<img src="https://lh7-us.googleusercontent.com/GtO8zrKLWnx0_9h3QRM_kiTEsxAEOS7ov4UkoKB40s_-1ZOCRlVXCQDF9PkWOOPz6lOfsBm9potD_PyfNNTiICI6hauQMnmkA--AfYaGBChL4e0bS6xlgX4aqOGXCIn5XskqFMUkMsGU6QQoxp6vFNo" width="700" />

Una vez dentro, solo seleccionamos el menú de Prometheus y buscamos la métrica a consultar, en este caso se selecciona una de mongo.

<img src="https://lh7-us.googleusercontent.com/Vv_ZCCGjAJVRdY9o9o_GOSD5SDArFxTcKkpUVs34gWOBYwGVLAusfPR4bMMjuMb3kLzxtxlMeP6eLd_ImGkN31GU-ILJ3El428iApFiOLvJfpq0R8H7nhGSZ8QteWxhIhMC3JOxh8HffT2ihbVPXfb0" width="700" />

<img src="https://lh7-us.googleusercontent.com/PxlxX6CxBTKnmxG8uYMMjPcWJXeqKMvGIGHzmwIATFnC2lcZsWz_aAiQRplJEClpo1c3kNqHThQ6UPi0t3fv6-zH9wzEeDHM8LbIWLxnzvQ65cZCukOIo_mFqtQG4ZafC7aOow37LYM2DScYKQHI4r4" width="700" />

Este es el proceso dentro de Prometheus, ahora podemos consultarlo desde Grafana. Una vez dentro seleccionamos la misma métrica que consultamos desde Prometheus, con la diferencia que podemos seleccionar la forma en la cual observar la gráfica, como se indica en el círculo rojo.

![](https://lh7-us.googleusercontent.com/Pu7O1WwR4C83exM-dLQFIJlQhFdJlXO8YPSbzEWSYbnRUV-IIS8w7xYnezH29R7dmO3eGS1WypByW0AMS-kswEuJLLOuLILd8pmcBV2pwXvHYpjINt9Z3_CiF9hDJvdfCBQP8G-1kbnZ-7C0Nzj8c7s)

![](https://lh7-us.googleusercontent.com/fLZwSoxgnud9AU6UrUmMMjnS2zrtgZLJ53Qy-X9m-ftYB5uTZ6EsJUiVaaDi_hdN4WPCkONh4QSlyfIVhLMr35uDxpxVQg19P2lH3UCPKZ5Sc4g8Mi35BlAie6UFZO7kLFi0J7ts0K9avkVgcYYzCOY)

![](https://lh7-us.googleusercontent.com/IXIpNr5-LMUiFSRxbSudQAktyP0plbk3xz-yxAaVvmyGMhZaUq73fsqJlBskhZ7etsrEseGUUp-W7kZEgiVlvibS_UojLhwQWoCAzZVBm9YVF4JHUBWfLeAH-mIesgVUSgpNWWImV2MBBiZCOGCVrNc)

 
# Resultados pruebas unitarias

Para las pruebas unitarias, se verificó la conexión con las bases de datos, para ello se ejecutó el test.py ubicado dentro del proyecto.

<img  src="https://lh7-us.googleusercontent.com/OLzy-lF-KoWr229xatYu7ZdQsfhDIf_OGYxbqBrCn6wlifSSwAWoz4xe_di_lvOcK9KcAl4SeHxCIaz8lz_OdDiIGPS7v6hWv-hoPTf5uNDGakXJwQ3IOZA-ywsEvBM-S4zBpigH6hZ5dTCL_1Bqu6w"  width="700"  />

Una vez ejecutado el archivo .py, este desplegará si la conexión con las bases de datos fue exitosa. La verificación de dicha conexión se concluye como cierta si el resultado de finalización es un OK, en este caso se comprueba que las conexiones son correctas.

<img  src="https://lh7-us.googleusercontent.com/aFuSy_uyccG8DpnbF2nLQHcPmtNHXX_v2RnkziqMwuZ98hRotiiuHSI6qXectwTv6OacJtF9k9j87xLpQvg28PBPbmvjUApqcukl5oBcNj3wuEXnF7Qdbx12HYbihnFGPchai_KJulRj3nucpruoOBo"  width="700"  />

El caso anterior es cuando ambas funcionan, pero si se hace un cambio que no permita la conexión, se desplegará un mensaje indicativo del fallo, como se muestra a continuación realizando un cambio en el URL de la conexión a Mongo.

<img  src="https://lh7-us.googleusercontent.com/pHxshzLi2cMT0wJTIQI0gO_bnb4vJ_ZPXjtAtZ4CvWB18PYHvE4CMnFn2PdsayDamSulX9_C79_jWMIWAfUm8Kp79hDYFPOLAYh62X9xRXZuG8pNV_XTO64N1bAIR4cNivaCvtzljpt7DbP-IWR-px4"  width="500"  />

Ahora, si se realiza un cambio en el URL de la conexión a Neo, como sustituir su puerto 7687 por 7686, podemos observar que aquí que se produce el fallo de conexión.

<img  src="https://lh7-us.googleusercontent.com/KQ-fwWpNibyjeUeYI1QLIoifSq5A0IKgTx09BEQo6ApA9p-DmkJamT0O9UjIJo6uhsnUKendZ8Xjaxv26SeBaXyHNmVchEVWC8382Idvr_uNhJCFR_4XciTG8XqCO25snAs5qxSq41agnoOa4kJnXGc"  width="500"  />

# Recomendaciones y conclusiones 

## Recomendaciones
1. Se recomienda utilizar un entorno de desarrollo como Visual Studio Code, ya que es práctico y permitirá ejecutar de manera sencilla cada una de las partes del programa.

2. Debe seguir los pasos indicados en el método de ejecución del programa, ya que realizarlos en otro orden puede ocasionar que ciertos elementos o el proyecto como tal no funcione.

3. La versión de python debe ser superior a la 3.10 debido a que posee un proceder distinto en diferentes instancias del código, esto principalmente si desea crear las imágenes usted mismo.

4. En caso de realizar modificaciones variadas, como agregar o quitar print para un pod y observarlo en el logs de Lens, debe ejecutar el app.py utilizando comandos de docker. En este caso, se recomienda limpiar el Dockerhub en línea, ya que en ocasiones daba error al crear imágenes y la solución que se encontró fue limpiarlo.

5. Si desea ejecutar el proyecto de manera local, debe considerar sustituir las variables que hacen conexiones. En este caso, se utilizan NodePort que son diferentes para cada pod, así que debe buscar dentro del Service en Lens el de cada pod, además considere que cada que hace una instalación nueva usando Helm, estos puertos pueden variar.

6. En caso de desinstalar el application se recomienda borrar los elementos del índice jobs y groups, esto porque puede presentar errores ya que pueden quedar valores intermedios de la anterior ejecución. Los comandos para ello, se encuentran dentro del proyecto en el archivo comandosElastic.txt.

7. En la carpeta dashboard dentro del proyecto, al querer ejecutar alguno de los ejemplos dentro del Grafana, van a presentar un error de ejecución, esto se debe a que cada archivo JSON que genera el Grafana contiene un id especial por cada inicio de sesión, así que se recomienda sustituir el id de cada JSON de ejemplo por el suyo y así pueda consultar los ejemplos.

8. Si consulta el Prometheus, puede en ocasiones no observar algunas métricas en específico, esto ocurre principalmente a la hora de instalar el application o el observability, dicho problema ocurre porque aún el proceso no ha llegado a Prometheus, por lo que se recomienda que, si ocurre dicho problema, se actualice la página pasados unos 30 segundos para así ver todas las métricas.

9. Si desinstala el observability debe considerar que al ejecutarlo nuevamente y abrir el Grafana, podrá observar que no tendrá el dashboard aún teniendo la conexión a Prometheus. El problema que ocurre es que se desvincula el service, por lo que deberá introducir el service nuevamente dentro del Grafana para así tener nuevamente el dashboard.

10. Debe realizar el proceso de sustitución de link en Thunkable cada vez que ejecute nuevamente el ngrok, ya que sino se realiza, la aplicación del Trunkable puede no mostrar datos debido a que está consultando un link viejo.


## Conclusiones

Para las conclusiones, se utilizarán las gráficas en formato JSON ubicadas dentro del proyecto, en este caso serán 4.
1. mongo_queries_sum:
- Time series:
<img  src="https://lh7-us.googleusercontent.com/GQETMvjrkRNzLfWnZVVQKP727JHpT1cUUfEIG4HCEIndtJ8nQ1c5Qh-hvMchGr-FB-SymRyVxeZxdLUbTXCpyswGMw0WpoPY-45E0xr6g5OvTd3GNZGSjb5qKNQU9F9VyLhf7GlYjOguKOeXjpdeKU8"  width="700"  />
- Bar chart:
<img  src="https://lh7-us.googleusercontent.com/jvVXL-p-0398m-I8qVk8NDo3qDxHbnPEyfTId4c7Lw1MC_P_sxX3nNPIvymFnf7Rx5RBvWi6kbqLTJirhPUGDQj5wS-uziHUU4WGmnA87nQPT3NiHTizJ16ShWFKHKSyJCxMj0SXPbxtBC86a0G-RN4"  width="700"  />
- Stat:
<img  src="https://lh7-us.googleusercontent.com/we9s2zKVY2qLDoU5OcF3y_MTKyDhgeUpqnDhLw1snB4lJ5smrs0mYitjVGGHtPt6Pb56p7cMlQ2otpXbgfYWqNIS1iXNPbt7feBBOBG1DFtzrXyXLY-u2Urm9dBOsmyUV6aX9jPNUCFobgVEK_gAaCU"  width="700"  />
- Table:
<img  src="https://lh7-us.googleusercontent.com/ti1-RLjzkGkPO44geLinXXOevU6eb3ZbR-gobMvx2j-bRkN1bBn2LJz3e_aOQ_Mxf_0O__Fg2TH3qFzI-0ZcpuLmwHqz3rKJeWru4bHxtyUvMF7mNnoXNKad_Itg8rOjVvYi08WFvDQiv6qYM67VqQs"  width="700"  />
- Pie chart:
<img  src="https://lh7-us.googleusercontent.com/LroZnnBtmaWDvcnpbJESqaKLNtFLI2lK_bcFCY63WdQb6RwF7CnWLAiC8caJmqwy4188IdFiDRVF9cgtQ3KlZRs29pbMgPnGPSGJnbOvdDD_N3kjzsVkhMD7mTz4PDm0G2g8Gb19JDM2kU33O30NulY"  width="700"  />

En este caso, las gráficas dejan en claro que se hizo una única consulta de búsqueda, principalmente en el área de filtrado. Aquí la que muestra la información con mayor claridad es la de Stat, ya que nos indica directamente el número de queries realizados en mongo.

2. mongo_queries_time:
- Time series:
<img  src="https://lh7-us.googleusercontent.com/hv9PU3T9tZZJnTIGl4ezzzRGRy_s_GchM45saH9HSskTF3hu9yOq8s5ojgvD3ZPj7O994P_TYZtr0NERQAdf4_8pEhtByyzIXrSy3DSCp8zGskSL639i2jbOVZgmy2CX43gNfqnsza3wAJSMdpzPdYk"  width="700"  />
- Bar chart:
<img  src="https://lh7-us.googleusercontent.com/TNg_2bmny4q4i4v4XAjYIgVBq4anXIqFraKfHdc02Rb6XgII4s08gnsvzzuwHt7OoOZ64xCNT2j7_9tEcUeyYugO3ECUQPs8W2QcfqRKS27A7T8xOww0NOLo_kTXU_sppUiJZOi12AdjsWcethDpIJE"  width="700"  />
- Stat:
<img  src="https://lh7-us.googleusercontent.com/EYFqJGTSy-FEWrydJlj50X6A06pP_x5NnC9rwHRxjN3rAUFaoiHg84-_WG1_c1oyfFa8vsCexW3wLzHrEs4sC151pummemDotD7PhQOeoqQ0qpFDPNPe4WYZDqw5xcMPztcLwcAA6ZK2gV-CMnVBYIE"  width="700"  />
- Table:
<img  src="https://lh7-us.googleusercontent.com/keUdRx9L3WRgnFckdJx1GxcA-9_OKEH_EDxsa4bajJOaUtmoeRqQbs80Rj6Ha_Qzdw2yghSWqFIlQnnt53Nl6KqFGBmbJXPulCVQWpVYPWAx5uspOq347ExI4jlPuqWE8gnv6_PcromER0HhNy2KnaM"  width="700"  />
- Pie chart:
<img  src="https://lh7-us.googleusercontent.com/0IPTBeXTHNXZAq7EhW317Bs601e-I5GYfcefJwgNW9TugNyGxyQlqNIKzd5R76DSAzGjoWfluE5MSmiV6GqZeN4xCnn3cNbCAi-eeA7XkZcXvce0aZ_-mcvTN9EqiHHBwUC4dIMvpxq4aYSmLQ_SCuQ"  width="700"  />

Las gráficas anteriores pareciera que no reflejan nada, incluso vemos unas vacías como Table y Pie, pero realmente hay datos, esto se logra apreciar gracias a gráficas como Time series y Bar chart, lo que deja la teoría de que los tiempos de consulta son tan rápidos y no logra generar las gráficas correspondientes, pero que sí existen.

3. neo4j_queries_sum:
- Time series:
<img  src="https://lh7-us.googleusercontent.com/azJeFbtDfW2fbO8KoEdxKlKLEr0UNfJDfQXQmgOT_ov_NnMT9pzi2zh6cqzY3xWEpc6-_eePmKG0VqcFCG46BxSdE08YF7LoYFQbihmfCkGQX2hBPpQxjqIPDNRB346_XFESdVJ16fHyT3A-KxbQ_Og"  width="700"  />
- Bar chart:
<img  src="https://lh7-us.googleusercontent.com/a7ZUkmU6_jkPew7XY4J3ZHcOJLN9IsKADFyG6J_eV6ZQFOGm_DIG8jfIzwK3IA4x-achA5yRcoEamnG9SKxV4bQdlLzprJ4u6HenrEx0U7gZ1KKS92SWKzQQJwRMTusg0hB3PaqT5ct1DNAR316E2VU"  width="700"  />
- Stat:
<img  src="https://lh7-us.googleusercontent.com/0ctGP3ybr1jFRZs1WfFgW5FHN8fKneUKSkiWT9Ok1PGN0l-Gz89S-xqXxYFyr0HfyyKQLSRrwf8Dw1c6gLREqm0WPOHP9C1d46LnWVhXG83YZ30R_nhjjhiN-k55pstxrXgmR6DPEdhhfvRmR9697Z8"  width="700"  />
- Table:
<img  src="https://lh7-us.googleusercontent.com/sYTnvleO_F9swNjcRa014W_YVb9JmEzJYRZNvdio_bnarog_BJ1CYeimDY2kqFc8rISJlNDE3-wkr73jICgW2Rw7HWYhh15sw_OlbGkbHOQYYIXBWEaipkFDEmkLFkTO3iDS5o_tfk64CdlbZQ789rg"  width="700"  />
- Pie chart:
<img  src="https://lh7-us.googleusercontent.com/tCLBb0EjeMoEt_G6T91Dw95PsKmUnZdM8w1cIfUH0iPVqPbr16X1yugdk0RQP8Y7wZLuCJvAKxhEX8bpXwzfyRAzTEYNCSPSpF6c8iaqwNapuyiQWkBKCqaz_y2Y-C_05DS2or6MgkCC1gUEm0wShRs"  width="700"  />

En este caso, las gráficas dejan en claro que se hizo una única consulta de búsqueda, principalmente en el área de filtrado. Aquí la que muestra la información con mayor claridad es la de Stat, ya que nos indica directamente el número de queries realizados en mongo. El caso particular respecto al de mongo, es que en la gráfica Table se sondeó un poco en la información hasta encontrar los datos, siendo reflejadas las consultas con su fecha y hora.

4. neo4j_queries_time:
- Time series:
<img  src="https://lh7-us.googleusercontent.com/uJIeVCfArKsdk_Folv3Kw3FM9RKR-yaw574mRN6HT_JZuqS5tV_Hmta0yACO0RypbkfJidO--Or4QzPbU2R57S35xIL8IcpCwcQTfzfu7Xu7atNa0AhsH6-nXcLU7HkmIiZUbcrWcWIpgazeXZ8eaDc"  width="700"  />
- Bar chart:
<img  src="https://lh7-us.googleusercontent.com/mTpqrJsekDvJ_R1DEhgNgGQ1S_-M-XWOkVfs1UzWKFxQOD4n9J6tzdUmAw9VnEPkLB9EGNz2T8c5tasAbNTZ32SVdT_kf3RSshvJARW4wk7a-doek7AKr2Uyj6kMIXlq_eFEtFUJXGh3Urp5EYZPZCk"  width="700"  />
- Stat:
<img  src="https://lh7-us.googleusercontent.com/EOT-BytggoVahnsaQtLdAUqpuV61QFxeoaYD1mwEIVyL1Bn95ZM5ZGA8Wgp5i9yQhF9XLTgLojQQXEWz70Zc2i_p4eg-q1CzkM4UqpIOTpyXavHgK7PTg5nVymgfOniNWOXGjykcPaQBJEyaIIbiaX4"  width="700"  />
- Table:
<img  src="https://lh7-us.googleusercontent.com/uVYGbUpKnzN1EL6MUdmmg0BZd8a4H7jr-sDoocsorXOqXTWiKFjAbixfL7gkb6dTZZ8sIdo_vovCwzb2A1uX7g8Zzlr4E5wCsp7SZPrimEX6uCCglefXrIGjODIs_vKEffQbnA0ycM1qZP3M8Fr4OJw"  width="700"  />
- Pie chart:
<img  src="https://lh7-us.googleusercontent.com/7i1e5d0Sy84A-gyYzLaXdA3uIVWi7y0Izf-W1r_idmA3BoVaoBmvKbXA5JWqM-850q9iEd8uN9TupnAv14CQ0TGXawcUwZ02maSzobu-zRD5OKAYSQHCrupKLDbqwwxlu09RQT5lMUoEEtkcvN_CCmE"  width="700"  />

Al igual que el de mongo, las gráficas anteriores pareciera que no reflejan nada, incluso vemos unas vacías como Table y Pie, pero realmente hay datos, esto se logra apreciar gracias a gráficas como Time series y Bar chart, lo que deja la teoría de que los tiempos de consulta son tan rápidos y no logra generar las gráficas correspondientes, pero que sí existen.

5. En conclusión, existen gráficas que son realmente útiles para reflejar el manejo de la información dentro del proceso automatizado, como lo es Stat, el cual indica los valores directamente en pantalla o incluso Table que muestra la cantidad de valores con su fecha y hora de ejecución, pero dichas gráficas parecen tener fallos a la hora de querer consultar valores más pequeños que unidades, mostrando supuestamente valores nulos, cuando en realidad aún existen valores, los cuales pueden ser vistos gracias a gráficas como Time series o Bar chart.

6. La interfaz de consultas se realiza mediante programación en bloques, lo que supone una experiencia interesante ya que siempre hemos programado con código como tal. Con esta programación uno aprende a realizar las cosas desde un punto de vista más gráfico y percatándose de lo que está realizando al momento.

7. Aunque ambas bases de datos contengan información de películas, no tienen la misma información, incluso hay algunas cuya información es incompleta. En el caso de Mongo, es muy completa, pero hay películas donde incluyen solo un grupo de los actores en vez de incluir a todos, o cómo Neo que incluye a todos los actores, pero su descripción de la película es muy incompleta.

8. Además de probar las bases de datos como Mongo y Neo, se prueba Firebase, la cual dice que es una base de datos en tiempo real, cosa que se puede evidenciar ya que a la hora de crear usuarios en el momento de ingresar por primera vez al sistema, este dato se muestra inmediatamente dentro de Firebase sin la necesidad de actualizar la página.

9. Para Mongo, es una base de datos interesante, tanto por ser NoSQL, como por el hecho de que puede ser manejada de manera gratuita desde el sitio web, en Atlas para ser específicos. Esto permite que sea una base de datos muy accesible y fácil de manejar comparada a otras como Elasticsearch que hay que montar tanto la base como a Kibana para poder manejarla.

10. La experiencia de utilizar nodos con Neo4j en vez de las tablas tradicionales es bastante única, porque las consultas se realizan según la entidad que deseas obtener y las relaciones que esta posee con otras entidades. Debido a esto las consultas terminan siendo bastante simples de realizar, el resultado de las consultas te puede devolver tanto las relaciones del nodo como los individuos con los que se relaciona, lo cual se puede observar de manera gráfica para facilitar su análisis.

# Referencias
Docker. “Get Started | Docker”. Docker. Accedido el 10 de abril de 2024. [En línea]. Disponible: [https://www.docker.com/get-started/](https://www.docker.com/get-started/)

Lens. “Lens | The Kubernetes IDE”. Lens | The Kubernetes IDE. Accedido el 10 de abril de 2024. [En línea]. Disponible: [https://k8slens.dev/](https://k8slens.dev/)

Python. “Download Python”. Python.org. Accedido el 10 de abril de 2024. [En línea]. Disponible: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Helm. “Installing Helm”. Helm. Accedido el 10 de abril de 2024. [En línea]. Disponible: [https://helm.sh/docs/intro/install/](https://helm.sh/docs/intro/install/)

DevOps Made Easy. Install Helm On Windows. (24 de octubre de 2022). Accedido el 10 de abril de 2024. [Video en línea]. Disponible: [https://www.youtube.com/watch?v=ZKAlKoqlWac](https://www.youtube.com/watch?v=ZKAlKoqlWac)

mattfarina. “Releases · helm/helm”. GitHub. Accedido el 10 de abril de 2024. [En línea]. Disponible: [https://github.com/helm/helm/releases](https://github.com/helm/helm/releases)

WinRAR. “Descargar WinRAR - Descarga gratuita recomendada”. Soporte WinRAR - Sitio oficial WinRAR en español. Accedido el 1 de abril de 2024. [En línea]. Disponible: [https://www.winrar.es/descargas](https://www.winrar.es/descargas)