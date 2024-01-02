class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        for row in image:
            row.reverse()

        for row in range(len(image)):

            for col in range(len(image[0])):
                if image[row][col]:
                    image[row][col]=0
                else:
                    image[row][col]=1
        return image


                