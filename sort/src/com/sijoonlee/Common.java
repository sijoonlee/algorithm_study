package com.sijoonlee;

class Common {
    public static int[] Copy(final int[] arr){
        int[] newArr = new int[arr.length];
        System.arraycopy(arr, 0, newArr, 0, arr.length);
        return newArr;
    }
    public static void Swap(int[] arr, int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    public static void Print(final int[] arr){
        System.out.println("--------------------");
        for(int elm: arr)
            System.out.print(elm + " ");
        System.out.println();
    }
}


/*
        int temp[] = new int[arr1.length];
        System.arraycopy(arr1, 0, temp, 0, arr1.length);

        for(int i=0; i< arr1.length; i++){
            temp[i] = arr1[i];
        }

        foreach (int elm : arr1){
        }
 */
