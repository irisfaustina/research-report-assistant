from typing import List, Optional, Dict, Any #to give exact format
from pydantic import BaseModel, Field

class Perspectives(BaseModel): #to create structured data models
    analysts: List[Analyst] = Field(
        description="Comprehensive of the analyst with their roles and affiliations."
    )