def is_valid_colab(colab):
  if all (key in colab for key in ("full_name", "departament", "dependents")):
    return True
  return False