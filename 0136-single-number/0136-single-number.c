int singleNumber(int* nums, int numsSize) {
    int result = nums[0];
    for(int i=0; i<numsSize; i++){
        int n=0;
        for(int j=0; j<numsSize; j++){
            if(i!=j && nums[i]==nums[j]){
                n++;
            }
        }
        if(n==0){
            result=nums[i];
        }
    }
    return result;
}