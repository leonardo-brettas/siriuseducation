from django.shortcuts import render
from pydantic import BaseModel, validator
from typing import List, Optional, Union, Dict
from abc import ABC, abstractmethod
from pandas import DataFrame

class Mamal(BaseModel, ABC):
    name: str
    age: int
    weight: float
    species: str
    individuals: List[List[int]]
    data: Optional[Union[DataFrame, List, Dict]]

    class Config:
        arbitrary_types_allowed = True

    @abstractmethod
    def speak(self):
        raise NotImplementedError

    @validator('data')
    def data_must_be_dataframe(cls, v):
        if isinstance(v, DataFrame):
          return v
        else:
            try:
                v = DataFrame(v)
                return v
            except:
                raise ValueError('data must be a DataFrame or convertible to a DataFrame')


class Dogs(Mamal):
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

    def speak(self):
        return "Woof"
# Create your views here.
