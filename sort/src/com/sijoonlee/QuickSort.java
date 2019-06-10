package com.sijoonlee;

public class QuickSort {
    public static int[] Run(int[] arr){
        int[] newArr = Common.Copy(arr);
        Recursion(newArr, 0, newArr.length-1);
        return newArr;
    }

    private static void Recursion(int[] arr, int begin, int end){
        if(begin < end){
            int dividingIndex = Partition(arr, begin, end);
            Recursion(arr, begin, dividingIndex-1);
            Recursion(arr, dividingIndex+1, end);
        }
    }

    private static int Partition(int[] arr, int begin, int end){
        int dividingElm = arr[end]; // set to the last element
        int dividingIndex = begin;
        for( int j = begin ; j < end ; j++){
            if(arr[j] <= dividingElm){
                Common.Swap(arr, dividingIndex, j); // swap element
                dividingIndex++; //push the dividing point to right
            }
        }
        Common.Swap(arr, dividingIndex, end);
        return dividingIndex;
    }

}
