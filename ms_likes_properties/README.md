# Habi Reto Parte 2

## Habi “Me gusta” MS

Para agregar una opción de "Me gusta" a las propiedades y permitir que los usuarios registrados les den Me gusta, debe agregar una nueva tabla llamada **property_likes**. La tabla tiene al menos dos columnas: una columna se usa para almacenar la ID del usuario al que le gustó, y la otra columna se usa para almacenar la ID del atributo que le gustó.

Este es el esquema de la tabla **property_likes**:

```sql
CREATE TABLE property_likes (
    user_id INT NOT NULL,
    property_id INT NOT NULL,
    PRIMARY KEY (user_id, property_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (property_id) REFERENCES property(id)
);
```

En este esquema, se utiliza una clave principal que consta de las columnas **user_id** y **property_id** para evitar que a los usuarios les guste la misma propiedad varias veces. Además, las claves externas se configuran para garantizar que los ID de usuario y de propiedad almacenados en la tabla **property_likes** se correspondan con ID válidos en las tablas **users** y **property**, respectivamente.

Aquí hay un ejemplo de cómo usar esta tabla en una consulta SQL para contar la cantidad de “Me gusta” para un atributo específico:

```sql
SELECT COUNT(*) FROM property_likes WHERE property_id = 3;
```

## Diagrama MER

![Untitled](Habi%20Challenge%20Part%202%2058b5f38bf6eb49a3ae66745e9100243b/Untitled.png)