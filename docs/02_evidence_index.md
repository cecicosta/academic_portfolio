# Evidence Index

Last updated: 2026-07-04

This index maps portfolio claims to local evidence files. It also records where
evidence is incomplete or still needs OCR/manual review.

## Experience-Level Status

This table supersedes the checkbox-style evidence index in the parent-folder RTF
drafts. Items are marked according to evidence currently present inside the
repository, plus public links that have been checked.

| Experience | Current support | Current status |
| --- | --- | --- |
| Student Association | Source note and scanned recommendation letter | Usable as a draft; public documentation and exact dates still missing |
| Academic Excellence Support Program | Source note and certificate image | Usable as a draft; original `Edital 18/2009` still missing from `sources/` |
| Virtual Shooting Training System | Source note, scanned recommendation letter, verified FUNCAP/UFC public pages, DOI to verify | Strongest current evidence set; OCR/manual letter review and publication capture still needed |
| Traffic Monitoring in Video Sequences | Source note and scanned official declaration | Usable as a draft; declaration needs OCR/manual review |
| Lenovo Diagnostics / LDiag | Source note and scanned recommendation letter | Usable as a draft with caveats; FCPC report and Lenovo manual still missing from `sources/` |
| Science Without Borders - South Korea | Source note, certificate images, StyleWiki internship certificate PDF | Usable as a draft; scholarship/enrollment/completion images need OCR/manual review |
| Augmented Reality for Remote Teaching of Manual Tasks | Source note, dissertation PDF, and article PDF | Usable as a draft; publication/coauthorship is supported locally, but role details still rely on the source note |
| ARTRADE - Augmented Reality Training Arcade | Source note | Usable as a draft with caveats; project was reportedly under NDA, so add primary role/project evidence if available |

## Local Evidence Files

| ID | Repository file | Evidence type | Supports | Review status |
| --- | --- | --- | --- | --- |
| E001 | `sources/declarations/recommendation_letter_creto_vidal_tiro_virtual.pdf` | Scanned recommendation letter | Virtual Shooting role and contributions | No extractable text; needs OCR/manual review |
| E002 | `sources/source_notes/virtual_shooting_training_system_overview.odt` | Local overview/source note | Technical context for Virtual Shooting project | Text extracted successfully from original; not a primary official record |
| E003 | `sources/declarations/declaracao_transito.pdf` | Scanned official declaration | Traffic Monitoring participation, dates, C/C++, computer vision work | No extractable text; details currently rely on prior draft and manual source note |
| E004 | `sources/source_notes/traffic_monitoring_video_sequences_overview.docx` | Local overview/source note | Traffic Monitoring project context and role summary | Text extracted successfully from original; not a primary official record |
| E005 | `sources/declarations/recommendation_letter_javam_machado_lenovo.pdf` | Scanned recommendation letter | Lenovo Diagnostics role and contributions | Minimal extractable text; needs OCR/manual review |
| E006 | `sources/source_notes/lenovo_diagnostics_project_overview.docx` | Local overview/source note | Lenovo Diagnostics project context and role summary | Text extracted successfully from original; supporting sources still to add |
| E007 | `sources/certificates/stylewiki_internship_certificate.pdf` | Certificate PDF | StyleWiki internship, July 4 to August 4, 2014, 102 hours | Text extraction confirms core certificate details; issued under former legal name |
| E008 | `sources/certificates/science_without_borders_certificate_of_enrollment.png` | Certificate image | Science Without Borders enrollment/exchange participation | Needs OCR/manual review |
| E009 | `sources/certificates/science_without_borders_certificate_of_completion.png` | Certificate image | Science Without Borders completion | Needs OCR/manual review |
| E010 | `sources/declarations/recommendation_letter_monteiro_student_association.pdf` | Scanned recommendation letter | Student Association leadership and representation | Minimal extractable text; needs OCR/manual review |
| E011 | `sources/source_notes/computer_science_student_association_overview.docx` | Local overview/source note | Student Association context and activities | Text extracted successfully from original; no public source found yet |
| E012 | `sources/source_notes/academic_excellence_support_program_overview.docx` | Local overview/source note | Academic Excellence Support Program context and duties | Text extracted successfully from original; original edital still to add |
| E013 | `sources/certificates/academic_excellence_mentoring_certificate.png` | Certificate image | Academic Excellence mentoring participation | Needs OCR/manual review |
| E014 | `sources/source_notes/science_without_borders_overview.docx` | Local overview/source note | Science Without Borders academic mobility context | Text extracted successfully from original; certificates still need OCR/manual review |
| E015 | `sources/source_notes/augmented_reality_manual_tasks_deaf_learners_overview.docx` | Local overview/source note | 2017 augmented reality/accessibility project role and responsibilities | Text extracted successfully from original; role details need primary confirmation |
| E016 | `sources/publications/thiago_araujo_macc_dissertation_2017.pdf` | Master's dissertation PDF | Research context for augmented reality, wearable devices, accessibility, and remote manual task instruction | Text extraction confirms title, institution, program, year, and research context |
| E017 | `sources/publications/analise_interacao_surdos_realidade_aumentada_dispositivos_vestiveis.pdf` | Article PDF | Coauthored publication on augmented reality interaction for deaf learners using wearable devices | Text extraction confirms title, authorship, abstract, and experiment context; venue not visible in PDF |
| E018 | `sources/source_notes/artrade_augmented_reality_training_arcade_overview.docx` | Local overview/source note | ARTRADE role, period, industry partner, and research/development responsibilities | Text extracted successfully from original; no primary/public project source added yet |

## Public References To Capture

| ID | Reference | Supports | Status |
| --- | --- | --- | --- |
| P001 | FUNCAP article: `https://www.funcap.ce.gov.br/2010/12/17/ceara-ganhara-sistema-de-treinamento-virtual-de-tiro/` | Virtual Shooting project origin, funding context, technical scope | Link verified in browser on 2026-07-04; consider saving PDF/archive |
| P002 | UFC article: `https://www.ufc.br/noticias/noticias-de-2012/1134-simulador-de-tiros-virtual-da-ufc-preparara-policiais-cearenses` | Virtual Shooting demonstration, participating UFC researchers, EXPOSEC presentation | Link verified in browser on 2026-07-04; consider saving PDF/archive |
| P003 | DOI `10.1109/SVR.2012.12` | SVR 2012 publication on the shooting training system | Listed in source draft; publication page still to verify/archive |
| P004 | FCPC 2014 annual report / project listing | Lenovo Diagnostics official project registration, GPF 3059, LDIAG FASE III | Mentioned in source draft; source file not yet present in repo |
| P005 | Lenovo Diagnostics Linux Bootable User Guide, version 4.33 | Product documentation and diagnostic module scope | Mentioned in source draft; source file not yet present in repo |

## Evidence Gaps

- Exact Student Association service dates.
- Original `Edital 18/2009` file for the Academic Excellence Support Program.
- OCR or manual transcription of recommendation letters and scanned
  declarations.
- Local copies or archived versions of the public Virtual Shooting references.
- Local copies of the Lenovo FCPC annual report and Lenovo Diagnostics manual.
- Primary ARTRADE evidence, such as a recommendation letter, project certificate,
  contract excerpt, or non-confidential institutional record.
- Publication venue or formal citation details for the augmented
  reality/accessibility article.
- Official transcript/diploma and language proof files, if intended for the
  application packet.

## Parent RTF Review Notes

The parent-folder files `00_context_for_codex.md.rtf`,
`01_timeline.md.rtf`, and `02_evidence_index.md.rtf` were reviewed on
2026-07-04. Their instructions are broadly consistent with this repository, but
some evidence statuses were optimistic relative to the files currently present in
`AcademicPortfolio/sources/`.

Corrections applied here:

- `Edital 18/2009` is treated as missing until the actual file is added.
- Lenovo FCPC registration and Lenovo Diagnostics manual are treated as pending
  until the source files are added.
- StyleWiki internship evidence is no longer pending because
  `sources/certificates/stylewiki_internship_certificate.pdf` is present and
  text extraction confirms the core dates and workload.
- Science Without Borders enrollment/completion evidence is present as images,
  but still needs OCR/manual review.
- Public Virtual Shooting pages were verified, but local archival copies should
  still be added for long-term dossier stability.
