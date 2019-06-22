package com.sijoonlee;

public class SelectionSort {
    public static int[] Run(int[] arr){
        int[] newArr = Common.Copy(arr);
        int length = newArr.length;

        for (int i = 0; i < length ; i++){
            int min = i;

            for (int j = i+1 ; j < length; j++)
                if(newArr[j] < newArr[min])
                    min = j;

            Common.Swap(newArr, i, min);
        }
        return newArr;
    }
}
