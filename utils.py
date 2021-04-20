## Utily functions for DEV Bull ##
from flask import jsonify


# def serialize(data):
#     """Serialize a number number or year data to dictionary."""

#     return {
#         "fact": data["text"],
#         "num": data["number"]

#     }

# def serialize_errors(errors):
#     """Serialize errors from SQLAlchemy obj to dictionary."""
#     # print(errors)
#     error_Dict = {}
#     error_Dict["errors"] =  { error: errors[error] for error in errors }

#     # print(error_Dict)
#     return error_Dict


# # print(serialize_errors({'year': ['Number must be between 1900 and 2000.'], 'color': ['Choose a color (red, blue, green or orange']}))