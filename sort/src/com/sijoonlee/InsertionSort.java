package com.sijoonlee;

public class InsertionSort {
    public static int[] Run(int[] arr){
        int[] newArr = Common.Copy(arr);
        int length = newArr.length;

        for (int i=0; i<length; i++){
            int cursor = newArr[i];
            int pos = i;

            while(pos>0 && newArr[pos-1]>cursor){
                newArr[pos] = newArr[pos-1];
                pos--;
            }
            newArr[pos] = cursor;
        }
        return newArr;
    }
}
