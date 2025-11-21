"""
Módulo para integrar la inteligencia artificial en las pruebas automatizadas.
Permite enviar mensajes o errores a la IA para recibir explicaciones, diagnósticos o sugerencias.
"""

#
# from openai import OpenAI
#
# client = OpenAI()
#
# def analizar_error_con_ia(error_texto: str) -> str:
#     #Envía el mensaje de error a la IA y devuelve una explicación y posible solución.
#
#     try:
#         respuesta = client.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=[
#                 {
#                     "role": "system",
#                     "content": (
#                         "Eres un experto en pruebas automatizadas con Appium, Selenium y Python. "
#                         "Tu tarea es analizar errores o excepciones y explicar la causa probable y cómo solucionarlos de forma corta"
#                     )
#                 },
#                 {
#                     "role": "user",
#                     "content": f"Analiza el siguiente error y explica su causa y solución:\n\n{error_texto}"
#                 }
#             ],
#             max_tokens=250
#         )
#
#         return respuesta.choices[0].message.content.strip()
#
#     except Exception as e:
#         return f"No se pudo conectar con la IA o procesar la respuesta: {e}"
#
#
# def sugerir_mejoras_test(descripcion_test: str) -> str:
#     #Usa la IA para sugerir mejoras o ideas de validaciones adicionales en un caso de prueba.
#
#     try:
#         respuesta = client.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=[
#                 {
#                     "role": "system",
#                     "content": (
#                         "Eres un experto en QA Automation. Analiza pruebas automatizadas y propone mejoras, "
#                         "validaciones adicionales o formas de optimizar el flujo de testing."
#                     )
#                 },
#                 {
#                     "role": "user",
#                     "content": f"Analiza este test y sugiere mejoras:\n\n{descripcion_test}"
#                 }
#             ],
#             max_tokens=300
#         )
#
#         return respuesta.choices[0].message.content.strip()
#
#     except Exception as e:
#         return f"No se pudo obtener sugerencias con IA: {e}"
