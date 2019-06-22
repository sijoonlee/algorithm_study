package com.sijoonlee;

public class MergeSort {

    public static int[] Run(int[] arr){
        int[] newArr = Common.Copy(arr);
        RecursiveDivide(newArr);
        return newArr;
    }

    private static void RecursiveDivide(int[] arr){
        int length = arr.length;
        if (length > 1){

            int halfLength = (length - length % 2)/2;
            // 10 -> midLength = 5
            // 9 -> midLength = 4

            int[] left = new int[halfLength];
            System.arraycopy(arr,0,left,0,halfLength);
            RecursiveDivide(left);

            int[] right = new int[length-halfLength];
            System.arraycopy(arr,halfLength,right,0,length-halfLength);
            RecursiveDivide(right);

            Merge(left, right, arr);
        }
    }

    private static void Merge(int[] left, int[] right, int[] arr){
        int leftIndex = 0;
        int rightIndex = 0;
        int leftLength = left.length;
        int rightLength = right.length;

        while(leftIndex < leftLength && rightIndex < rightLength){
            if(left[leftIndex] <= right[rightIndex]) {
                arr[leftIndex + rightIndex] = left[leftIndex];
                leftIndex++;
            } else {
                arr[leftIndex + rightIndex] = right[rightIndex];
                rightIndex++;
            }
        }
        for(; leftIndex< leftLength; leftIndex++){
            arr[leftIndex+rightIndex] = left[leftIndex];
        }
        for(; rightIndex < rightLength; rightIndex++){
            arr[leftIndex+rightIndex] = right[rightIndex];
        }
    }
}
