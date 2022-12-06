/*
Ejercicio 4: Crear una matriz de tamaño 7x7 y rellenarla de forma que los 
elementos de la diagonal principal sean 1 y el resto 0.
 */
package matriz_Ejercicio_4;

public class Matriz_Ejercicio_4 {
    public static void main(String[] args) {
        int matriz [][] = new int [7][7];
        
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                if(i == j){
                    matriz [i][j] = 1;
                }
                else{
                    matriz[i][j] = 0;
                }
            }
        }
        System.out.println();
        
        System.out.println("Matriz con diagonal principal en 1 y el resto en 0: ");
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {     
                System.out.print(matriz [i][j]+" ");  
            }
            System.out.println();
        }
        System.out.println();
    }
}
