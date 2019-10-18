# modify this function, and create other functions below as you wish
def question01(initialLevelOfDebt, interestPercentage, repaymentPercentage):
    # modify and then return the variable below
    count=0
    while initialLevelOfDebt > 50:
        interestPercentage = (5/100)*initialLevelOfDebt
        initialLevelOfDebt=(initialLevelOfDebt+interestPercentage)-repaymentPercentage
        count=count+1
    answer = (count * repaymentPercentage)+initialLevelOfDebt+repaymentPercentage
    return answer
initialLevelOfDebt = int(input("enter the Initial Level Of Debt :"))
interestPercentage=0
repaymentPercentage=(10/100)*initialLevelOfDebt
ans = question01(initialLevelOfDebt, interestPercentage, repaymentPercentage)
print(round(ans))
