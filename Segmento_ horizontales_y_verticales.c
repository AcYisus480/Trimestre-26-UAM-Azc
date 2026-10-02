#include <stdio.h>

int main(){
    int segmento_1[4], segmento_2[4];

    for (int i = 0; i < 8; i++){
        if (i < 4){ 
            scanf("%d", &segmento_1[i]);
        }else{
            scanf("%d", &segmento_2[i-4]);
        }
    }

// Calcular orientación

    int orientacion_S1, orientacion_S2;

    if(segmento_1[0]==segmento_1[2]){
        // H
        orientacion_S1 = 0;
    } else{
        // V
        orientacion_S1 = 1;
    }

    if(segmento_2[0]==segmento_2[2]){
        // H
        orientacion_S2 = 0;
    } else{
        // V
        orientacion_S2 = 1;
    }


// Puntos de intersección

    // Uno es Vertical y el otro orizontal
    int x, y;
    int x_1 = segmento_1[0];
    int y_1 = segmento_1[1];
    int x_2 = segmento_1[2];
    int y_2 = segmento_1[3];
    int x_3 = segmento_2[0];
    int y_3 = segmento_2[1];
    int x_4 = segmento_2[2];
    int y_4 = segmento_2[3];
    
    if(orientacion_S1 == 1 && orientacion_S2 == 0){
        if(x_1 <= x_3 && x_2 >= x_4 && y_3 <= y_1 && y_4 >= y_2 ){
            y = segmento_1[1];
            x= segmento_2[0];
        }else{
            x = -1;
            y = -1;
        }
    }else{
        if(segmento_2[0] <= segmento_1[0] && segmento_2[2] >= segmento_1[2]){
            y = segmento_2[1];
            x= segmento_1[0];
        }else{
            x = -1;
            y = -1;
        }
    }

    printf("%d %d %d %d", orientacion_S1, orientacion_S2, x, y);
    
    return 0;
}