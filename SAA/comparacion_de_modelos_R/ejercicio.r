setwd('./SAA/comparacion_de_modelos_R')

# importar df
df <- read.csv("./housing.csv", stringsAsFactors = FALSE)
str(df)

any(is.na(df))
# hay nulos
colSums(is.na(df))
# nulos en dormitorios

# eliminar nulos
df$total_bedrooms[is.na(df$total_bedrooms)] <- median(df$total_bedrooms, na.rm = TRUE)

# comprobar nulos
any(is.na(df))
# no hay nulos

# convertir columna proximidad al mar en una columna categorica
df$ocean_proximity <- as.factor(df$ocean_proximity)

# crear columnas que derivan de otras columnas
# habitaciones por personas que viven juntos
df$rooms_per_household <- df$total_rooms / df$households
# dormitorios por habitaciones
df$bedrooms_per_room <- df$total_bedrooms / df$total_rooms
# personas por 'nucelos familiares'
df$population_per_household <- df$population / df$households

#resumen estadistico de nuestro df
summary(df)

# instalar ggplot
install.packages("ggplot2")
library(ggplot2)

# grafica distribuicion de precios
ggplot(df, aes(x = median_house_value)) + geom_histogram(fill="skyblue", color="black", bins=30) + labs(title="Distribución del Precio de Viviendas", x="Precio", y="Frecuencia")
# datos sesgados a la derecha con outlier al final de la grafica

# instalar dplyr
# install.packages("dplyr")
install.packages("tidyverse")
library(tidyverse)

# matriz de correlacion de columnas numericas
num_vars <- df %>% select(where(is.numeric))
corr_matrix <- cor(num_vars)

# instalar corrplot
install.packages("corrplot")
library(corrplot)

corrplot(corr_matrix, method="circle", type="upper")
# vemos que solo median_income tiene notable relacion con nuestra variable objetivo

# MODELO REGRESION LINEAL
set.seed(42)
train_index <- sample(1:nrow(df), size = 0.8*nrow(df))
train_data <- df[train_index, ]
test_data  <- df[-train_index, ]

modelo_lm <- lm(median_house_value ~ ., data = train_data)
summary(modelo_lm)

# vemos en residuals valores como el valor max que se equivoco por arriba y por abajo, la media, y el error entre cuartiles 1q 3q
# vemos en coefficients la correlacion interpretada
# r-squared, 64.95% de la variabilidad del precio de viviendas, meh
# un f-statistic alto (2038) indica que el modelo en general es valido y que al menos una de las variables tiene un efecto en median_house_value
# el p-valor es pequeno, el modelo tiene una relacion significativa con los precios

# EVALUACION DEL MODELO
pred_lm <- predict(modelo_lm, newdata = test_data)
R2_test <- cor(pred_lm, test_data$median_house_value)^2
RMSE_test <- sqrt(mean((pred_lm - test_data$median_house_value)^2))
MAE_test <- mean(abs(pred_lm - test_data$median_house_value))

cat("R²:", R2_test, "\nRMSE:", RMSE_test, "USD\nMAE:", MAE_test, "USD\n")

# tenemos un r2 "positivo", el modelo explica bien la variabilidad del precio
# hay un error medio de 48k, que al tener en cuenta que la media de las casas esta en 180k, el modelo es mas bien tirando a bueno

# MODELO RANDOM FOREST

# instalar randomforest
install.packages("randomForest")
library(randomForest)

modelo_rf <- randomForest(median_house_value ~ ., data = train_data, ntree = 100)
pred_rf <- predict(modelo_rf, newdata = test_data)

R2_rf <- cor(pred_rf, test_data$median_house_value)^2
RMSE_rf <- sqrt(mean((pred_rf - test_data$median_house_value)^2))
MAE_rf <- mean(abs(pred_rf - test_data$median_house_value))

cat("Random Forest\nR²:", R2_rf, "\nRMSE:", RMSE_rf, "USD\nMAE:", MAE_rf, "USD\n")

# vemos una grandisima mejora usando random forest
# con un r2 de .82, mucho mas cercano a 1
# y con un error medio de 31k, mejor que el del modelo anterior
