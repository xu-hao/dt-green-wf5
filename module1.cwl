cwlVersion: v1.0
class: CommandLineTool

baseCommand: python

requirements:
  InitialWorkDirRequirement:
    listing:
      - class: File
        location: module1.py
      - class: File
        location: workflow5.py
  InlineJavascriptRequirement: {}

arguments:
  - module1.py

stdout: retval

inputs: []

outputs:
  - id: cohort_id
    type: string
    outputBinding:
        glob: retval
        loadContents: true
        outputEval: $(self[0].contents.trim())
