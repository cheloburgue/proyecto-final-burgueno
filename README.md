# proyecto-final-burgueno

Description:

EL PROGRAMA MUESTRA UNA PAGINA WEB DE UN BLOG PARA SUBIR LUGARES DEL MUNDO, VISUALIZAR UN HOME CON TODOS LOS POST Y PODER LOGUEARSE PARA PODER AGREGAR PUBLICACIONES, EDITARLAS O ELIMINARLAS, EDITAR EL PERFIL DE USUARIO Y EL AVATAR Y PODER REALIZAR COMENTARIOS SOBRE CADA PUBLICACION DEL BLOG.

------------------------------------------------------------------------------------------------------------------------------------------------------

1 - Clonar el repositorio de GitHub localmente en la carpeta deseada mediante el comando:
      -> git clone https://github.com/cheloburgue/proyecto-final-burgueno
      
------------------------------------------------------------------------------------------------------------------------------------------------------
      
2 - Abrimos Visual Studio code y en la terminal en caso de no tenerlo instalado corremos el siguiente comando para instalar Django(en caso de ya tenerlo omitir el paso 2)
      -> pip install django
      
------------------------------------------------------------------------------------------------------------------------------------------------------

3 - Una vez instalado nos paramos sobre la carpeta raiz del proyecto importado '../tercera-pre-entrega-burgueno>' y ejecutamos el siguiente comando:
      -> python manage.py runserver
      
    Este comando levantara un servidor local para poder visualizar la pagina correctamente
------------------------------------------------------------------------------------------------------------------------------------------------------

4 - Una vez levantado el servidor deberemos ingresar a la siguiente ruta local (Vease en la consola el IP del servidor que acabamos de levantar) 
      
       http://127.0.0.1:8000/AppCoder/   (Agregarle el tag a la url  /AppCoder/ para poder visualizar correctamente la pagina web.

------------------------------------------------------------------------------------------------------------------------------------------------------

5 - Ya tenemos acceso a la Web! La misma cuanta con 5 secciones.

- Home -> Pagina de inicio donde se visulizan los post de todos los usuarios. Esta permite ver los post e ingresar al detalle de los mismos y los comentarios.
- Acerca de mi -> muestra una breve descripcion del objetivo de la pagina.
- boton Login -> Se hace el ingreso a la pagina o en su defecto se puede registrar para poder acceder.

-- Una vez logueado
Se visualizan los siguientes botones
- boton Mis Post -> Permite visualizar el listado de post propios del usuario logueado, en caso que no se haya subido ninguno se visualizara un mensaje de que no existen publicaciones. En caso que se tenga acceso, es posible ver el detalle, editar o eliminar publicaciones y/o visualizar o agregar comentarios a las mismas. (Se pueden hacer estas opciones tanto desde Mis Post como desde el HOME (Editar y Eliminar solo lo podran hacer solo en aquellas publicaciones propias del usuario Logueado)
- boton Agregar Post -> Permite agregar publicaciones que luego se veran sobre la seccion de mis post, solo las propias del usuario y en Home se veran junto con el listado general de publicaciones.
- boton Perfil -> Se puede ver y editar la informacion del usuario y se le puede agregar un avatar a eleccion al perfil.

--------------------------------------------------------------------------------------------------------------------------------------------------

6 - Para poder validar las cargas a la base de datos se puede ingresar al Backoffice de administrador en el siguiente enlace:
      http://127.0.0.1:8000/admin

      usuario : admin
      pass: admin
