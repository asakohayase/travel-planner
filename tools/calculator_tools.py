from typing import Any
from crewai_tools import BaseTool
from pydantic.v1 import BaseModel, Field


class CalculatorInput(BaseModel):
    operation: str = Field(
        ..., description="The mathematical expression to be evaluated."
    )


class CalculatorTools(BaseTool):
    name: str = "Make a calculation"
    description: str = (
        "Useful to perform any mathematical calculations, "
        "like sum, minus, multiplication, division, etc. "
        "The input should be a mathematical expression, "
        "e.g., '200*7' or '5000/2*10'"
    )
    args_schema: type[BaseModel] = CalculatorInput

    def _run(self, operation: str) -> Any:
        try:
            return eval(operation)
        except SyntaxError:
            return "Error: Invalid syntax in mathematical expression"
        except (NameError, TypeError):
            return "Error: Invalid operation or use of undefined variables"
        except ZeroDivisionError:
            return "Error: Division by zero"
        except Exception as e:
            return f"Error: An unexpected error occurred - {str(e)}"


# Usage example:
# calculator = CalculatorTools()
# result = calculator.run("200*7")
# print(result)  # Output: 1400
