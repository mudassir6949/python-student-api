from pydantic import BaseModel, Field


class StudentCreate(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=100
    )

    age: int = Field(
        ge=5,
        le=100
    )

    course: str = Field(
        min_length=2,
        max_length=100
    )


class StudentUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=2,
        max_length=100
    )

    age: int | None = Field(
        default=None,
        ge=5,
        le=100
    )

    course: str | None = Field(
        default=None,
        min_length=2,
        max_length=100
    )


class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    course: str

    class Config:
        from_attributes = True