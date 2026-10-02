#include <stdio.h>

void ordenar(int *a, int *b)
{
    if (*a > *b)
    {
        int tem = *a;
        *a = *b;
        *b = tem;
    }
}

int en_rango(int val, int min, int max)
{
    return val >= min && val <= max;
}

int main()
{

    int x, y;
    int x_1, x_2, x_3, x_4, y_1, y_2, y_3, y_4;

    scanf("%d %d %d %d %d %d %d %d", &x_1, &y_1, &x_2, &y_2, &x_3, &y_3, &x_4, &y_4);

    // Calcular orientación

    int orientacion_S1, orientacion_S2;

    if (x_1 == x_2)
    {
        // V
        orientacion_S1 = 0;
    }
    else
    {
        // H
        orientacion_S1 = 1;
    }

    if (x_3 == x_4)
    {
        // V
        orientacion_S2 = 0;
    }
    else
    {
        // H
        orientacion_S2 = 1;
    }

    // Puntos de intersección

    ordenar(&x_1, &x_2);
    ordenar(&y_1, &y_2);
    ordenar(&x_3, &x_4);
    ordenar(&y_3, &y_4);

    if ((orientacion_S1 == 1 && orientacion_S2 == 0) || (orientacion_S1 == 0 && orientacion_S2 == 1))
    {
        if (en_rango(x_4, x_1, x_2) && en_rango(y_1, y_3, y_4))
        {
            y = y_1;
            x = x_3;
        }
        else if (en_rango(x_1, x_3, x_4) && en_rango(y_3, y_1, y_2))
        {
            y = y_3;
            x = x_1;
        }
        else
        {
            x = -1;
            y = -1;
        }
    }
    else if (orientacion_S1 == 1 && orientacion_S2 == 1)
    {
        if (y_1 == y_4 && en_rango(x_3, x_1, x_2) && en_rango(x_2, x_3, x_4))
        {
            x = x_3;
            y = y_1;
        }
        else if (y_1 == y_4 && en_rango(x_4, x_1, x_2) && en_rango(x_1, x_3, x_4))
        {
            x = x_4;
            y = y_1;
        }
        else
        {
            x = -1;
            y = -1;
        }
    }
    else if (orientacion_S1 == 0 && orientacion_S2 == 0)
    {
        if (x_1 == x_4 && en_rango(y_3, y_1, y_2) && en_rango(y_2, y_3, y_4))
        {
            x = x_3;
            y = y_1;
        }
        else if (x_1 == x_4 && en_rango(y_1, y_3, y_4) && en_rango(y_4, y_1, y_2))
        {
            x = x_4;
            y = y_1;
        }
        else
        {
            x = -1;
            y = -1;
        }
    }
    else
    {
        x = -1;
        y = -1;
    }

    printf("%d %d %d %d", orientacion_S1, orientacion_S2, x, y);

    return 0;
}