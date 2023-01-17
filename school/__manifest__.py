# See LICENSE file for full copyright and licensing details.

{
    "name": "School",
    "version": "16.0.1.0.0",
    "author": "Serpent Consulting Services Pvt. Ltd.",
    "website": "http://www.serpentcs.com",
    "category": "School Management",
    "license": "AGPL-3",
    "complexity": "easy",
    "Summary": "A Module For School Management",
    "images": ["static/description/EMS.jpg"],
    "depends": ["hr", "crm", "account"],
    "data": [
        "security/school_security.xml",
        "security/ir.model.access.csv",
        "data/student_sequence.xml",
        "data/mail_template.xml",
        "wizard/terminate_reason_view.xml",
        "views/student_view.xml",
        "views/school_view.xml",
        "views/teacher_view.xml",
        "views/parent_view.xml",
        "wizard/assign_roll_no_wizard.xml",
        "wizard/move_standards_view.xml",
        "report/report_view.xml",
        "report/identity_card.xml",
        "report/leaving_certificate.xml",
        "report/teacher_identity_card.xml",
    ],
    "demo": ["demo/school_demo.xml"],
    "assets": {
        "web.assets_backend": ["/school/static/src/scss/schoolcss.scss"]
    },
    "installable": True,
    "application": True,
}
