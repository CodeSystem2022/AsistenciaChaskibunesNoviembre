/*
Ejercicio 3: Crear y cargar una matriz de tamaño 3x3, trasponerla y mostrarla.
*/
package matriz_Ejercicio_3;

import java.util.Scanner;

public class Matriz_Ejercicio_3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int matriz [][] = new int [3][3];
        
        System.out.println("Rellenar la matriz: ");
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.println("Digite el valor de la matriz ["+i+"]["+j+"]:");
                matriz [i][j] = entrada.nextInt();
            }
        }
        System.out.println();
        
        System.out.println("Matriz Original: ");
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {     
                System.out.print(matriz [i][j]+" ");  
            }
            System.out.println();
        }
        System.out.println();
         
        System.out.println("Matriz Transpuesta: ");
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.print(matriz [j][i]+" ");  
            }
            System.out.println();
        }
        System.out.println();
    }
}
