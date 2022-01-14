
#Bubble Sort
def bubblesort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp


nums = [4, 2, 8, 9, 5]
bubblesort(nums)

print('Bubblesort:', nums)

#Selection Sort
def selectionsort(nums1):
    for i in range(len(nums1)-1):
        minpos = i
        for j in range(i, len(nums1)):
            if nums1[j] < nums1[minpos]:
                minpos = j

        temp = nums1[i]
        nums1[i] = nums1[minpos]
        nums1[minpos] = temp

nums1 = [3, 5, 8, 2, 5, 6]
selectionsort(nums1)

print('Selectionsort:', nums1)

#InsertionSort / fkt nicht richtig
def insertionsort(nums2):
    for i in range(1, len(nums2)):
        j = i
        while nums2[j -1] > nums2[j] and j > 0:
            nums2[j - 1], nums2[j] = nums2[j], nums2[j -1]
            j -= 1

nums2 = [4, 2, 1, 5, 7, 9]
insertionsort(nums2)

print('Insertionsort:', insertionsort(nums2))