#include <stdio.h>

float calcular_costo(int clave, int min)
{
    switch (clave)
    {
    case 12:
        return 2 * min;
    case 15:
        return 2.2 * min;
    case 18:
        return 4.5 * min;
    case 19:
        return 3.5 * min;
    case 23:
        return 6 * min;
    case 25:
        return 6 * min;
    case 29:
        return 5 * min;
    }
}

int main()
{
    int clave, min;
    float total[5];

    for (int i = 0; i < 5; i++)
    {
        scanf(" %d , %d", &clave, &min);
        total[i] = calcular_costo(clave, min);
    }

    for (int i = 0; i < 5; i++)
    {
        if (total[i] == (int)total[i])
        {
            printf("%d\n", (int)total[i]);
        }
        else
        {
            printf("%.1f\n", total[i]);
        }
    }
    return 0;
}