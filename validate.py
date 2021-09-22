def is_valid_colab(colab):
  if ("full_name", "departament", "dependents") in colab.items():
    return True
  return False