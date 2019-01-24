cwlVersion: v1.0
class: CommandLineTool

baseCommand: python

requirements:
  InitialWorkDirRequirement:
    listing:
      - class: File
        location: module2_4_question2.py
      - class: File
        location: workflow5.py
  InlineJavascriptRequirement: {}

arguments:
  - module2_4_question2.py

stdout: retval

inputs:
  - id: cohort_id
    type: string
    inputBinding:
      prefix: '--cohort_id'
  - id: maximum_p_value
    type: float
    inputBinding:
      prefix: '--maximum_p_value'

outputs:
  - id: features
    type: string
    outputBinding:
      glob: retval
      loadContents: true
      outputEval: $(self[0].contents.trim())
        
