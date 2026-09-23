# API del Hospital Provincial Arroyo Claro

Estado del hospital el día de la misión: camas, guardias, turnos, farmacia y espera en la guardia. Nada de esto está en los documentos de `datos/corpus/`.

```bash
python3 api/servidor.py          # http://localhost:8765
```

Todas las rutas son `GET` y devuelven JSON. Los nombres no distinguen mayúsculas ni tildes, y los espacios equivalen a guiones bajos.

| Ruta | Parámetro | Devuelve |
|---|---|---|
| `/camas` | `sector` | total, ocupadas y libres del sector |
| `/guardia` | `especialidad` | profesionales de guardia hoy y su horario |
| `/turnos` | `especialidad` | próximos turnos disponibles (fecha y hora) |
| `/farmacia` | `medicamento` | stock y, si no hay, fecha de reposición |
| `/espera` | ninguno | minutos de espera actuales por nivel de triage |

Un nombre inexistente o un parámetro faltante devuelve un error con la lista de opciones válidas, así el agente puede corregirse.

```bash
curl "http://localhost:8765/camas?sector=pediatria"
curl "http://localhost:8765/farmacia?medicamento=enalapril%2010%20mg"
```
