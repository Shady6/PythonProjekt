from abc import ABCMeta, abstractmethod

class Converter(metaclass=ABCMeta):
    @property
    @abstractmethod
    def conversions(self):
        pass

    # A -> B

    def ConvertAndFillResultLabel(self, isAToB, unitAName, unitBName, value, resultValueLabel):
        value = float(value)
        result = self.Convert(isAToB, unitAName, unitBName, value)
        resultValueLabel["text"] = str(result)

    def Convert(self, isAToB, unitAName, unitBName, value):
        if isAToB:
            return self.A_to_B(unitAName, unitBName, value)
        else:
            return self.B_to_A(unitAName, unitBName, value)

    def A_to_B(self, unitAName, unitBName, value):
        middle_B = self.A_to_middle_B(unitAName, value)
        return self.Middle_B_to_B(unitBName, middle_B)

    def A_to_middle_B(self, unitAName, value):
        A_to_middle_A = self.conversions["unit_A"]["A_to_middle_A"]

        if unitAName not in A_to_middle_A:
            return self.conversions["unit_A"]["middle_A_to_middle_B"](value)
        else:
            middle_A = A_to_middle_A[unitAName](value)
            return self.conversions["unit_A"]["middle_A_to_middle_B"](middle_A)

    def Middle_B_to_B(self, unitBName, value):
        middle_B_to_B = self.conversions["unit_B"]["middle_B_to_B"]

        if unitBName not in middle_B_to_B:
            return value
        else:
            return middle_B_to_B[unitBName](value)

    # B -> A

    def B_to_A(self, unitAName, unitBName, value):
        middle_A = self.B_to_middle_A(unitBName, value)
        return self.Middle_A_to_A(unitAName, middle_A)

    def B_to_middle_A(self, unitBName, value):
        B_to_middle_B = self.conversions["unit_B"]["B_to_middle_B"]

        if unitBName not in B_to_middle_B:
            return self.conversions["unit_B"]["middle_B_to_middle_A"](value)
        else:
            middle_B = B_to_middle_B[unitBName](value)
            return self.conversions["unit_B"]["middle_B_to_middle_A"](middle_B)

    def Middle_A_to_A(self, unitAName, value):
        middle_A_to_A = self.conversions["unit_A"]["middle_A_to_A"]

        if unitAName not in middle_A_to_A:
            return value
        else:
            return middle_A_to_A[unitAName](value)
