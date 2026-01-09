# 获取联系人信息

# 通讯协议如下

## Head

Request URL
http://mem.deep-diary.com/vaults/019ba163-d71f-70d0-b3cc-f8a53413f24b/contacts/019ba163-d7a3-72b5-96b5-ba4ea81c0406/tabs/information
Request Method
GET
Status Code
200 OK
Remote Address
112.17.30.188:80
Referrer Policy
strict-origin-when-cross-origin

## payload

## response

<!DOCTYPE html>
<html lang="zh-CN" dir="ltr">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="csrf-token" content="w3l9ZBieozIgu9wHpNwQHGU0XJpDv9akrYsJufBU">
        <title inertia>Monica</title>
        <link rel="shortcut icon" href="/img/favicon.svg">
        <!-- Scripts -->
        <script type="text/javascript">
            if (localStorage.theme === 'dark' || (!('theme'in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
                document.documentElement.classList.add('dark')
            } else {
                document.documentElement.classList.remove('dark')
            }
        </script>
        <script type="text/javascript">
            const Ziggy = {
                "url": "http:\/\/mem.deep-diary.com",
                "port": null,
                "defaults": {},
                "routes": {
                    "webauthn.auth.options": {
                        "uri": "webauthn\/auth\/options",
                        "methods": ["POST"]
                    },
                    "webauthn.auth": {
                        "uri": "webauthn\/auth",
                        "methods": ["POST"]
                    },
                    "webauthn.store.options": {
                        "uri": "webauthn\/keys\/options",
                        "methods": ["POST"]
                    },
                    "webauthn.store": {
                        "uri": "webauthn\/keys",
                        "methods": ["POST"]
                    },
                    "webauthn.destroy": {
                        "uri": "webauthn\/keys\/{id}",
                        "methods": ["DELETE"],
                        "parameters": ["id"]
                    },
                    "webauthn.update": {
                        "uri": "webauthn\/keys\/{id}",
                        "methods": ["PUT"],
                        "parameters": ["id"]
                    },
                    "scribe": {
                        "uri": "docs",
                        "methods": ["GET", "HEAD"]
                    },
                    "scribe.postman": {
                        "uri": "docs.postman",
                        "methods": ["GET", "HEAD"]
                    },
                    "scribe.openapi": {
                        "uri": "docs.openapi",
                        "methods": ["GET", "HEAD"]
                    },
                    "login": {
                        "uri": "login",
                        "methods": ["GET", "HEAD"]
                    },
                    "login.store": {
                        "uri": "login",
                        "methods": ["POST"]
                    },
                    "logout": {
                        "uri": "logout",
                        "methods": ["POST"]
                    },
                    "password.request": {
                        "uri": "forgot-password",
                        "methods": ["GET", "HEAD"]
                    },
                    "password.reset": {
                        "uri": "reset-password\/{token}",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["token"]
                    },
                    "password.email": {
                        "uri": "forgot-password",
                        "methods": ["POST"]
                    },
                    "password.update": {
                        "uri": "reset-password",
                        "methods": ["POST"]
                    },
                    "register": {
                        "uri": "register",
                        "methods": ["GET", "HEAD"]
                    },
                    "register.store": {
                        "uri": "register",
                        "methods": ["POST"]
                    },
                    "verification.notice": {
                        "uri": "email\/verify",
                        "methods": ["GET", "HEAD"]
                    },
                    "verification.verify": {
                        "uri": "email\/verify\/{id}\/{hash}",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["id", "hash"]
                    },
                    "verification.send": {
                        "uri": "email\/verification-notification",
                        "methods": ["POST"]
                    },
                    "user-profile-information.update": {
                        "uri": "user\/profile-information",
                        "methods": ["PUT"]
                    },
                    "user-password.update": {
                        "uri": "user\/password",
                        "methods": ["PUT"]
                    },
                    "password.confirm": {
                        "uri": "user\/confirm-password",
                        "methods": ["GET", "HEAD"]
                    },
                    "password.confirmation": {
                        "uri": "user\/confirmed-password-status",
                        "methods": ["GET", "HEAD"]
                    },
                    "password.confirm.store": {
                        "uri": "user\/confirm-password",
                        "methods": ["POST"]
                    },
                    "two-factor.login": {
                        "uri": "two-factor-challenge",
                        "methods": ["GET", "HEAD"]
                    },
                    "two-factor.login.store": {
                        "uri": "two-factor-challenge",
                        "methods": ["POST"]
                    },
                    "two-factor.enable": {
                        "uri": "user\/two-factor-authentication",
                        "methods": ["POST"]
                    },
                    "two-factor.confirm": {
                        "uri": "user\/confirmed-two-factor-authentication",
                        "methods": ["POST"]
                    },
                    "two-factor.disable": {
                        "uri": "user\/two-factor-authentication",
                        "methods": ["DELETE"]
                    },
                    "two-factor.qr-code": {
                        "uri": "user\/two-factor-qr-code",
                        "methods": ["GET", "HEAD"]
                    },
                    "two-factor.secret-key": {
                        "uri": "user\/two-factor-secret-key",
                        "methods": ["GET", "HEAD"]
                    },
                    "two-factor.recovery-codes": {
                        "uri": "user\/two-factor-recovery-codes",
                        "methods": ["GET", "HEAD"]
                    },
                    "terms.show": {
                        "uri": "terms-of-service",
                        "methods": ["GET", "HEAD"]
                    },
                    "policy.show": {
                        "uri": "privacy-policy",
                        "methods": ["GET", "HEAD"]
                    },
                    "profile.show": {
                        "uri": "user\/profile",
                        "methods": ["GET", "HEAD"]
                    },
                    "other-browser-sessions.destroy": {
                        "uri": "user\/other-browser-sessions",
                        "methods": ["DELETE"]
                    },
                    "current-user-photo.destroy": {
                        "uri": "user\/profile-photo",
                        "methods": ["DELETE"]
                    },
                    "api-tokens.index": {
                        "uri": "user\/api-tokens",
                        "methods": ["GET", "HEAD"]
                    },
                    "api-tokens.store": {
                        "uri": "user\/api-tokens",
                        "methods": ["POST"]
                    },
                    "api-tokens.update": {
                        "uri": "user\/api-tokens\/{token}",
                        "methods": ["PUT"],
                        "parameters": ["token"]
                    },
                    "api-tokens.destroy": {
                        "uri": "user\/api-tokens\/{token}",
                        "methods": ["DELETE"],
                        "parameters": ["token"]
                    },
                    "sanctum.csrf-cookie": {
                        "uri": "sanctum\/csrf-cookie",
                        "methods": ["GET", "HEAD"]
                    },
                    "sabre.dav": {
                        "uri": "dav\/{path?}",
                        "methods": ["GET", "HEAD", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "GET", "HEAD", "POST", "PUT", "PATCH", "DELETE", "PROPFIND", "PROPPATCH", "MKCOL", "COPY", "MOVE", "LOCK", "UNLOCK", "OPTIONS", "REPORT", "GET", "HEAD", "POST", "PUT", "PATCH", "DELETE", "PROPFIND", "PROPPATCH", "MKCOL", "COPY", "MOVE", "LOCK", "UNLOCK", "OPTIONS", "REPORT"],
                        "wheres": {
                            "path": "(.)*"
                        },
                        "parameters": ["path"]
                    },
                    "api.": {
                        "uri": "api\/user",
                        "methods": ["GET", "HEAD"]
                    },
                    "api.users.index": {
                        "uri": "api\/users",
                        "methods": ["GET", "HEAD"]
                    },
                    "api.users.show": {
                        "uri": "api\/users\/{user}",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["user"]
                    },
                    "api.vaults.index": {
                        "uri": "api\/vaults",
                        "methods": ["GET", "HEAD"]
                    },
                    "api.vaults.store": {
                        "uri": "api\/vaults",
                        "methods": ["POST"]
                    },
                    "api.vaults.show": {
                        "uri": "api\/vaults\/{vault}",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault"]
                    },
                    "api.vaults.update": {
                        "uri": "api\/vaults\/{vault}",
                        "methods": ["PUT", "PATCH"],
                        "parameters": ["vault"]
                    },
                    "api.vaults.destroy": {
                        "uri": "api\/vaults\/{vault}",
                        "methods": ["DELETE"],
                        "parameters": ["vault"]
                    },
                    "home": {
                        "uri": "\/",
                        "methods": ["GET", "HEAD"]
                    },
                    "login.provider": {
                        "uri": "auth\/{driver}",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["driver"]
                    },
                    "invitation.show": {
                        "uri": "invitation\/{code}",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["code"]
                    },
                    "invitation.store": {
                        "uri": "invitation",
                        "methods": ["POST"]
                    },
                    "vault.index": {
                        "uri": "vaults",
                        "methods": ["GET", "HEAD"]
                    },
                    "vault.create": {
                        "uri": "vaults\/create",
                        "methods": ["GET", "HEAD"]
                    },
                    "vault.store": {
                        "uri": "vaults",
                        "methods": ["POST"]
                    },
                    "vault.show": {
                        "uri": "vaults\/{vault}",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault"],
                        "bindings": {
                            "vault": "id"
                        }
                    },
                    "vault.edit": {
                        "uri": "vaults\/{vault}\/edit",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault"],
                        "bindings": {
                            "vault": "id"
                        }
                    },
                    "vault.update": {
                        "uri": "vaults\/{vault}",
                        "methods": ["PUT"],
                        "parameters": ["vault"],
                        "bindings": {
                            "vault": "id"
                        }
                    },
                    "vault.destroy": {
                        "uri": "vaults\/{vault}",
                        "methods": ["DELETE"],
                        "parameters": ["vault"],
                        "bindings": {
                            "vault": "id"
                        }
                    },
                    "vault.default_tab.update": {
                        "uri": "vaults\/{vault}\/defaultTab",
                        "methods": ["PUT"],
                        "parameters": ["vault"]
                    },
                    "vault.calendar.index": {
                        "uri": "vaults\/{vault}\/calendar",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault"],
                        "bindings": {
                            "vault": "id"
                        }
                    },
                    "vault.calendar.month": {
                        "uri": "vaults\/{vault}\/calendar\/years\/{year}\/months\/{month}",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "year", "month"],
                        "bindings": {
                            "vault": "id"
                        }
                    },
                    "vault.calendar.day": {
                        "uri": "vaults\/{vault}\/calendar\/years\/{year}\/months\/{month}\/days\/{day}",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "year", "month", "day"],
                        "bindings": {
                            "vault": "id"
                        }
                    },
                    "vault.reminder.index": {
                        "uri": "vaults\/{vault}\/reminders",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault"]
                    },
                    "vault.feed.show": {
                        "uri": "vaults\/{vault}\/feed",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault"]
                    },
                    "vault.tasks.index": {
                        "uri": "vaults\/{vault}\/tasks",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault"]
                    },
                    "vault.reports.index": {
                        "uri": "vaults\/{vault}\/reports",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault"]
                    },
                    "vault.reports.addresses.index": {
                        "uri": "vaults\/{vault}\/reports\/addresses",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault"]
                    },
                    "vault.reports.addresses.cities.show": {
                        "uri": "vaults\/{vault}\/reports\/addresses\/city\/{city}",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "city"]
                    },
                    "vault.reports.addresses.countries.show": {
                        "uri": "vaults\/{vault}\/reports\/addresses\/country\/{country}",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "country"]
                    },
                    "vault.reports.mood_tracking_events.index": {
                        "uri": "vaults\/{vault}\/reports\/moodTrackingEvents",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault"]
                    },
                    "vault.reports.important_dates.index": {
                        "uri": "vaults\/{vault}\/reports\/importantDates",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault"]
                    },
                    "vault.life_metrics.store": {
                        "uri": "vaults\/{vault}\/lifeMetrics",
                        "methods": ["POST"],
                        "parameters": ["vault"]
                    },
                    "vault.life_metrics.update": {
                        "uri": "vaults\/{vault}\/lifeMetrics\/{metric}",
                        "methods": ["PUT"],
                        "parameters": ["vault", "metric"]
                    },
                    "vault.life_metrics.contact.store": {
                        "uri": "vaults\/{vault}\/lifeMetrics\/{metric}",
                        "methods": ["POST"],
                        "parameters": ["vault", "metric"]
                    },
                    "vault.life_metrics.destroy": {
                        "uri": "vaults\/{vault}\/lifeMetrics\/{metric}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "metric"]
                    },
                    "contact.index": {
                        "uri": "vaults\/{vault}\/contacts",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault"],
                        "bindings": {
                            "vault": "id"
                        }
                    },
                    "contact.label.index": {
                        "uri": "vaults\/{vault}\/contacts\/labels\/{label}",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "label"]
                    },
                    "contact.sort.update": {
                        "uri": "vaults\/{vault}\/contacts\/sort",
                        "methods": ["PUT"],
                        "parameters": ["vault"],
                        "bindings": {
                            "vault": "id"
                        }
                    },
                    "contact.create": {
                        "uri": "vaults\/{vault}\/contacts\/create",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault"],
                        "bindings": {
                            "vault": "id"
                        }
                    },
                    "contact.store": {
                        "uri": "vaults\/{vault}\/contacts",
                        "methods": ["POST"],
                        "parameters": ["vault"]
                    },
                    "contact.show": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.edit": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/edit",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.update": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}",
                        "methods": ["POST"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.destroy": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.vcard.download": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/vcard",
                        "methods": ["POST"],
                        "parameters": ["vault", "contact"],
                        "bindings": {
                            "vault": "id",
                            "contact": "id"
                        }
                    },
                    "contact.quick_fact.show": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/quickFacts\/{template}",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "contact", "template"]
                    },
                    "contact.quick_fact.store": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/quickFacts\/{template}",
                        "methods": ["POST"],
                        "parameters": ["vault", "contact", "template"]
                    },
                    "contact.quick_fact.toggle": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/quickFacts\/toggle",
                        "methods": ["PUT"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.quick_fact.update": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/quickFacts\/{template}\/{quickFact}",
                        "methods": ["PUT"],
                        "parameters": ["vault", "contact", "template", "quickFact"]
                    },
                    "contact.quick_fact.destroy": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/quickFacts\/{template}\/{quickFact}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "contact", "template", "quickFact"]
                    },
                    "contact.archive.update": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/toggle",
                        "methods": ["PUT"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.favorite.update": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/toggle-favorite",
                        "methods": ["PUT"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.move.show": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/move",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.move.store": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/move",
                        "methods": ["POST"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.blank": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/update-template",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.template.update": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/template",
                        "methods": ["PUT"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.page.show": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/tabs\/{slug}",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "contact", "slug"]
                    },
                    "contact.avatar.update": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/avatar",
                        "methods": ["PUT"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.avatar.destroy": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/avatar",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.feed.show": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/feed",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.date.index": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/dates",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.date.store": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/dates",
                        "methods": ["POST"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.date.update": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/dates\/{date}",
                        "methods": ["PUT"],
                        "parameters": ["vault", "contact", "date"]
                    },
                    "contact.date.destroy": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/dates\/{date}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "contact", "date"]
                    },
                    "contact.note.index": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/notes",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.note.store": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/notes",
                        "methods": ["POST"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.note.update": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/notes\/{note}",
                        "methods": ["PUT"],
                        "parameters": ["vault", "contact", "note"]
                    },
                    "contact.note.destroy": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/notes\/{note}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "contact", "note"]
                    },
                    "contact.goal.show": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/goals\/{goal}",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "contact", "goal"]
                    },
                    "contact.goal.store": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/goals",
                        "methods": ["POST"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.goal.update": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/goals\/{goal}",
                        "methods": ["PUT"],
                        "parameters": ["vault", "contact", "goal"]
                    },
                    "contact.goal.streak.update": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/goals\/{goal}\/streaks",
                        "methods": ["PUT"],
                        "parameters": ["vault", "contact", "goal"]
                    },
                    "contact.goal.destroy": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/goals\/{goal}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "contact", "goal"]
                    },
                    "contact.label.store": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/labels",
                        "methods": ["POST"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.label.update": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/labels\/{label}",
                        "methods": ["PUT"],
                        "parameters": ["vault", "contact", "label"]
                    },
                    "contact.label.destroy": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/labels\/{label}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "contact", "label"]
                    },
                    "contact.reminder.store": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/reminders",
                        "methods": ["POST"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.reminder.update": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/reminders\/{reminder}",
                        "methods": ["PUT"],
                        "parameters": ["vault", "contact", "reminder"]
                    },
                    "contact.reminder.destroy": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/reminders\/{reminder}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "contact", "reminder"]
                    },
                    "contact.address.store": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/addresses",
                        "methods": ["POST"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.address.update": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/addresses\/{address}",
                        "methods": ["PUT"],
                        "parameters": ["vault", "contact", "address"]
                    },
                    "contact.address.destroy": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/addresses\/{address}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "contact", "address"]
                    },
                    "contact.address.image.show": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/addresses\/{address}\/image\/{width}x{height}",
                        "methods": ["GET", "HEAD"],
                        "wheres": {
                            "width": ".*",
                            "height": ".*"
                        },
                        "parameters": ["vault", "contact", "address", "width", "height"]
                    },
                    "contact.contact_information.store": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/contactInformation",
                        "methods": ["POST"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.contact_information.update": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/contactInformation\/{info}",
                        "methods": ["PUT"],
                        "parameters": ["vault", "contact", "info"]
                    },
                    "contact.contact_information.destroy": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/contactInformation\/{info}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "contact", "info"]
                    },
                    "contact.loan.store": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/loans",
                        "methods": ["POST"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.loan.update": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/loans\/{loan}",
                        "methods": ["PUT"],
                        "parameters": ["vault", "contact", "loan"]
                    },
                    "contact.loan.toggle": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/loans\/{loan}\/toggle",
                        "methods": ["PUT"],
                        "parameters": ["vault", "contact", "loan"]
                    },
                    "contact.loan.destroy": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/loans\/{loan}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "contact", "loan"]
                    },
                    "contact.companies.list.index": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/companies\/list",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.job_information.update": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/jobInformation",
                        "methods": ["PUT"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.job_information.destroy": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/jobInformation",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.religion.update": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/religion",
                        "methods": ["PUT"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.relationships.create": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/relationships\/create",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.relationships.store": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/relationships",
                        "methods": ["POST"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.relationships.update": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/relationships\/{relationship}",
                        "methods": ["PUT"],
                        "parameters": ["vault", "contact", "relationship"]
                    },
                    "contact.pet.store": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/pets",
                        "methods": ["POST"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.pet.update": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/pets\/{pet}",
                        "methods": ["PUT"],
                        "parameters": ["vault", "contact", "pet"]
                    },
                    "contact.pet.destroy": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/pets\/{pet}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "contact", "pet"]
                    },
                    "contact.document.store": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/documents",
                        "methods": ["POST"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.document.destroy": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/documents\/{document}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "contact", "document"]
                    },
                    "contact.photo.index": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/photos",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.photo.show": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/photos\/{photo}",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "contact", "photo"]
                    },
                    "contact.photo.store": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/photos",
                        "methods": ["POST"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.photo.destroy": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/photos\/{photo}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "contact", "photo"]
                    },
                    "contact.task.index": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/tasks\/completed",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.task.store": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/tasks",
                        "methods": ["POST"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.task.update": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/tasks\/{task}",
                        "methods": ["PUT"],
                        "parameters": ["vault", "contact", "task"]
                    },
                    "contact.task.toggle": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/tasks\/{task}\/toggle",
                        "methods": ["PUT"],
                        "parameters": ["vault", "contact", "task"]
                    },
                    "contact.task.destroy": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/tasks\/{task}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "contact", "task"]
                    },
                    "contact.call.store": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/calls",
                        "methods": ["POST"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.call.update": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/calls\/{call}",
                        "methods": ["PUT"],
                        "parameters": ["vault", "contact", "call"]
                    },
                    "contact.call.destroy": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/calls\/{call}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "contact", "call"]
                    },
                    "contact.group.store": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/groups",
                        "methods": ["POST"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.group.destroy": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/groups\/{group}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "contact", "group"]
                    },
                    "contact.timeline_event.index": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/timelineEvents",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.timeline_event.store": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/timelineEvents",
                        "methods": ["POST"],
                        "parameters": ["vault", "contact"]
                    },
                    "contact.timeline_event.toggle": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/timelineEvents\/{timelineEvent}\/toggle",
                        "methods": ["POST"],
                        "parameters": ["vault", "contact", "timelineEvent"]
                    },
                    "contact.life_event.store": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/timelineEvents\/{timelineEvent}\/lifeEvents",
                        "methods": ["POST"],
                        "parameters": ["vault", "contact", "timelineEvent"]
                    },
                    "contact.timeline_event.destroy": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/timelineEvents\/{timelineEvent}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "contact", "timelineEvent"]
                    },
                    "contact.life_event.edit": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/timelineEvents\/{timelineEvent}\/lifeEvents\/{lifeEvent}",
                        "methods": ["PUT"],
                        "parameters": ["vault", "contact", "timelineEvent", "lifeEvent"]
                    },
                    "contact.life_event.toggle": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/timelineEvents\/{timelineEvent}\/lifeEvents\/{lifeEvent}\/toggle",
                        "methods": ["POST"],
                        "parameters": ["vault", "contact", "timelineEvent", "lifeEvent"]
                    },
                    "contact.life_event.destroy": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/timelineEvents\/{timelineEvent}\/lifeEvents\/{lifeEvent}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "contact", "timelineEvent", "lifeEvent"]
                    },
                    "contact.mood_tracking_event.store": {
                        "uri": "vaults\/{vault}\/contacts\/{contact}\/moodTrackingEvents",
                        "methods": ["POST"],
                        "parameters": ["vault", "contact"]
                    },
                    "group.index": {
                        "uri": "vaults\/{vault}\/groups",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault"]
                    },
                    "group.show": {
                        "uri": "vaults\/{vault}\/groups\/{group}",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "group"]
                    },
                    "group.edit": {
                        "uri": "vaults\/{vault}\/groups\/{group}\/edit",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "group"]
                    },
                    "group.update": {
                        "uri": "vaults\/{vault}\/groups\/{group}",
                        "methods": ["PUT"],
                        "parameters": ["vault", "group"]
                    },
                    "group.destroy": {
                        "uri": "vaults\/{vault}\/groups\/{group}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "group"]
                    },
                    "journal.index": {
                        "uri": "vaults\/{vault}\/journals",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault"],
                        "bindings": {
                            "vault": "id"
                        }
                    },
                    "journal.create": {
                        "uri": "vaults\/{vault}\/journals\/create",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault"],
                        "bindings": {
                            "vault": "id"
                        }
                    },
                    "journal.store": {
                        "uri": "vaults\/{vault}\/journals",
                        "methods": ["POST"],
                        "parameters": ["vault"]
                    },
                    "journal.show": {
                        "uri": "vaults\/{vault}\/journals\/{journal}",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "journal"]
                    },
                    "journal.photo.index": {
                        "uri": "vaults\/{vault}\/journals\/{journal}\/photos",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "journal"]
                    },
                    "journal.year": {
                        "uri": "vaults\/{vault}\/journals\/{journal}\/years\/{year}",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "journal", "year"]
                    },
                    "journal.edit": {
                        "uri": "vaults\/{vault}\/journals\/{journal}\/edit",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "journal"]
                    },
                    "journal.update": {
                        "uri": "vaults\/{vault}\/journals\/{journal}",
                        "methods": ["PUT"],
                        "parameters": ["vault", "journal"]
                    },
                    "journal.destroy": {
                        "uri": "vaults\/{vault}\/journals\/{journal}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "journal"]
                    },
                    "post.create": {
                        "uri": "vaults\/{vault}\/journals\/{journal}\/posts\/create",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "journal"]
                    },
                    "post.store": {
                        "uri": "vaults\/{vault}\/journals\/{journal}\/posts\/template\/{template}",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "journal", "template"]
                    },
                    "post.show": {
                        "uri": "vaults\/{vault}\/journals\/{journal}\/posts\/{post}",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "journal", "post"]
                    },
                    "post.edit": {
                        "uri": "vaults\/{vault}\/journals\/{journal}\/posts\/{post}\/edit",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "journal", "post"]
                    },
                    "post.update": {
                        "uri": "vaults\/{vault}\/journals\/{journal}\/posts\/{post}\/update",
                        "methods": ["PUT"],
                        "parameters": ["vault", "journal", "post"]
                    },
                    "post.photos.store": {
                        "uri": "vaults\/{vault}\/journals\/{journal}\/posts\/{post}\/photos",
                        "methods": ["POST"],
                        "parameters": ["vault", "journal", "post"]
                    },
                    "post.photos.destroy": {
                        "uri": "vaults\/{vault}\/journals\/{journal}\/posts\/{post}\/photos\/{photo}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "journal", "post", "photo"]
                    },
                    "post.destroy": {
                        "uri": "vaults\/{vault}\/journals\/{journal}\/posts\/{post}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "journal", "post"]
                    },
                    "post.tag.store": {
                        "uri": "vaults\/{vault}\/journals\/{journal}\/posts\/{post}\/tags",
                        "methods": ["POST"],
                        "parameters": ["vault", "journal", "post"]
                    },
                    "post.tag.update": {
                        "uri": "vaults\/{vault}\/journals\/{journal}\/posts\/{post}\/tags\/{tag}",
                        "methods": ["PUT"],
                        "parameters": ["vault", "journal", "post", "tag"]
                    },
                    "post.tag.destroy": {
                        "uri": "vaults\/{vault}\/journals\/{journal}\/posts\/{post}\/tags\/{tag}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "journal", "post", "tag"]
                    },
                    "post.slices.update": {
                        "uri": "vaults\/{vault}\/journals\/{journal}\/posts\/{post}\/slices",
                        "methods": ["PUT"],
                        "parameters": ["vault", "journal", "post"]
                    },
                    "post.slices.destroy": {
                        "uri": "vaults\/{vault}\/journals\/{journal}\/posts\/{post}\/slices",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "journal", "post"]
                    },
                    "post.metrics.store": {
                        "uri": "vaults\/{vault}\/journals\/{journal}\/posts\/{post}\/metrics",
                        "methods": ["POST"],
                        "parameters": ["vault", "journal", "post"]
                    },
                    "post.metrics.destroy": {
                        "uri": "vaults\/{vault}\/journals\/{journal}\/posts\/{post}\/metrics\/{metric}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "journal", "post", "metric"]
                    },
                    "slices.index": {
                        "uri": "vaults\/{vault}\/journals\/{journal}\/slices",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "journal"]
                    },
                    "slices.store": {
                        "uri": "vaults\/{vault}\/journals\/{journal}\/slices",
                        "methods": ["POST"],
                        "parameters": ["vault", "journal"]
                    },
                    "slices.show": {
                        "uri": "vaults\/{vault}\/journals\/{journal}\/slices\/{slice}",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "journal", "slice"]
                    },
                    "slices.edit": {
                        "uri": "vaults\/{vault}\/journals\/{journal}\/slices\/{slice}\/edit",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "journal", "slice"]
                    },
                    "slices.update": {
                        "uri": "vaults\/{vault}\/journals\/{journal}\/slices\/{slice}",
                        "methods": ["PUT"],
                        "parameters": ["vault", "journal", "slice"]
                    },
                    "slices.cover.update": {
                        "uri": "vaults\/{vault}\/journals\/{journal}\/slices\/{slice}\/cover",
                        "methods": ["PUT"],
                        "parameters": ["vault", "journal", "slice"]
                    },
                    "slices.cover.destroy": {
                        "uri": "vaults\/{vault}\/journals\/{journal}\/slices\/{slice}\/cover",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "journal", "slice"]
                    },
                    "slices.destroy": {
                        "uri": "vaults\/{vault}\/journals\/{journal}\/slices\/{slice}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "journal", "slice"]
                    },
                    "journal_metrics.index": {
                        "uri": "vaults\/{vault}\/journals\/{journal}\/metrics",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "journal"]
                    },
                    "journal_metrics.store": {
                        "uri": "vaults\/{vault}\/journals\/{journal}\/metrics",
                        "methods": ["POST"],
                        "parameters": ["vault", "journal"]
                    },
                    "journal_metrics.destroy": {
                        "uri": "vaults\/{vault}\/journals\/{journal}\/metrics\/{metric}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "journal", "metric"]
                    },
                    "vault.files.index": {
                        "uri": "vaults\/{vault}\/files",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault"]
                    },
                    "vault.files.photos": {
                        "uri": "vaults\/{vault}\/files\/photos",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault"]
                    },
                    "vault.files.documents": {
                        "uri": "vaults\/{vault}\/files\/documents",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault"]
                    },
                    "vault.files.avatars": {
                        "uri": "vaults\/{vault}\/files\/avatars",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault"]
                    },
                    "vault.files.destroy": {
                        "uri": "vaults\/{vault}\/files\/{file}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "file"]
                    },
                    "vault.companies.index": {
                        "uri": "vaults\/{vault}\/companies",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault"]
                    },
                    "vault.companies.show": {
                        "uri": "vaults\/{vault}\/companies\/{company}",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault", "company"]
                    },
                    "vault.settings.index": {
                        "uri": "vaults\/{vault}\/settings",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault"]
                    },
                    "vault.settings.update": {
                        "uri": "vaults\/{vault}\/settings",
                        "methods": ["PUT"],
                        "parameters": ["vault"]
                    },
                    "vault.settings.template.update": {
                        "uri": "vaults\/{vault}\/settings\/template",
                        "methods": ["PUT"],
                        "parameters": ["vault"]
                    },
                    "vault.settings.user.store": {
                        "uri": "vaults\/{vault}\/settings\/users",
                        "methods": ["POST"],
                        "parameters": ["vault"]
                    },
                    "vault.settings.user.update": {
                        "uri": "vaults\/{vault}\/settings\/users\/{user}",
                        "methods": ["PUT"],
                        "parameters": ["vault", "user"]
                    },
                    "vault.settings.user.destroy": {
                        "uri": "vaults\/{vault}\/settings\/users\/{user}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "user"]
                    },
                    "vault.settings.label.index": {
                        "uri": "vaults\/{vault}\/settings\/labels",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault"]
                    },
                    "vault.settings.label.store": {
                        "uri": "vaults\/{vault}\/settings\/labels",
                        "methods": ["POST"],
                        "parameters": ["vault"]
                    },
                    "vault.settings.label.update": {
                        "uri": "vaults\/{vault}\/settings\/labels\/{label}",
                        "methods": ["PUT"],
                        "parameters": ["vault", "label"]
                    },
                    "vault.settings.label.destroy": {
                        "uri": "vaults\/{vault}\/settings\/labels\/{label}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "label"]
                    },
                    "vault.settings.tag.index": {
                        "uri": "vaults\/{vault}\/settings\/tags",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault"]
                    },
                    "vault.settings.tag.store": {
                        "uri": "vaults\/{vault}\/settings\/tags",
                        "methods": ["POST"],
                        "parameters": ["vault"]
                    },
                    "vault.settings.tag.update": {
                        "uri": "vaults\/{vault}\/settings\/tags\/{tag}",
                        "methods": ["PUT"],
                        "parameters": ["vault", "tag"]
                    },
                    "vault.settings.tag.destroy": {
                        "uri": "vaults\/{vault}\/settings\/tags\/{tag}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "tag"]
                    },
                    "vault.settings.important_date_type.store": {
                        "uri": "vaults\/{vault}\/settings\/contactImportantDateTypes",
                        "methods": ["POST"],
                        "parameters": ["vault"]
                    },
                    "vault.settings.important_date_type.update": {
                        "uri": "vaults\/{vault}\/settings\/contactImportantDateTypes\/{type}",
                        "methods": ["PUT"],
                        "parameters": ["vault", "type"]
                    },
                    "vault.settings.important_date_type.destroy": {
                        "uri": "vaults\/{vault}\/settings\/contactImportantDateTypes\/{type}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "type"]
                    },
                    "vault.settings.tab.update": {
                        "uri": "vaults\/{vault}\/settings\/visibility",
                        "methods": ["PUT"],
                        "parameters": ["vault"]
                    },
                    "vault.settings.mood_tracking_parameter.store": {
                        "uri": "vaults\/{vault}\/settings\/moodTrackingParameters",
                        "methods": ["POST"],
                        "parameters": ["vault"]
                    },
                    "vault.settings.mood_tracking_parameter.update": {
                        "uri": "vaults\/{vault}\/settings\/moodTrackingParameters\/{parameter}",
                        "methods": ["PUT"],
                        "parameters": ["vault", "parameter"]
                    },
                    "vault.settings.mood_tracking_parameter.order.update": {
                        "uri": "vaults\/{vault}\/settings\/moodTrackingParameters\/{parameter}\/order",
                        "methods": ["PUT"],
                        "parameters": ["vault", "parameter"]
                    },
                    "vault.settings.mood_tracking_parameter.destroy": {
                        "uri": "vaults\/{vault}\/settings\/moodTrackingParameters\/{parameter}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "parameter"]
                    },
                    "vault.settings.life_event_categories.store": {
                        "uri": "vaults\/{vault}\/settings\/lifeEventCategories",
                        "methods": ["POST"],
                        "parameters": ["vault"]
                    },
                    "vault.settings.life_event_categories.update": {
                        "uri": "vaults\/{vault}\/settings\/lifeEventCategories\/{lifeEventCategory}",
                        "methods": ["PUT"],
                        "parameters": ["vault", "lifeEventCategory"]
                    },
                    "vault.settings.life_event_categories.destroy": {
                        "uri": "vaults\/{vault}\/settings\/lifeEventCategories\/{lifeEventCategory}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "lifeEventCategory"]
                    },
                    "vault.settings.life_event_categories.order.update": {
                        "uri": "vaults\/{vault}\/settings\/lifeEventCategories\/{lifeEventCategory}\/order",
                        "methods": ["POST"],
                        "parameters": ["vault", "lifeEventCategory"]
                    },
                    "vault.settings.life_event_types.store": {
                        "uri": "vaults\/{vault}\/settings\/lifeEventCategories\/{lifeEventCategory}\/lifeEventTypes",
                        "methods": ["POST"],
                        "parameters": ["vault", "lifeEventCategory"]
                    },
                    "vault.settings.life_event_types.update": {
                        "uri": "vaults\/{vault}\/settings\/lifeEventCategories\/{lifeEventCategory}\/lifeEventTypes\/{lifeEventType}",
                        "methods": ["PUT"],
                        "parameters": ["vault", "lifeEventCategory", "lifeEventType"]
                    },
                    "vault.settings.life_event_types.destroy": {
                        "uri": "vaults\/{vault}\/settings\/lifeEventCategories\/{lifeEventCategory}\/lifeEventTypes\/{lifeEventType}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "lifeEventCategory", "lifeEventType"]
                    },
                    "vault.settings.life_event_types.order.update": {
                        "uri": "vaults\/{vault}\/settings\/lifeEventCategories\/{lifeEventCategory}\/lifeEventTypes\/{lifeEventType}\/order",
                        "methods": ["POST"],
                        "parameters": ["vault", "lifeEventCategory", "lifeEventType"]
                    },
                    "vault.settings.quick_fact_templates.store": {
                        "uri": "vaults\/{vault}\/settings\/quickFactTemplates",
                        "methods": ["POST"],
                        "parameters": ["vault"]
                    },
                    "vault.settings.quick_fact_templates.update": {
                        "uri": "vaults\/{vault}\/settings\/quickFactTemplates\/{template}",
                        "methods": ["PUT"],
                        "parameters": ["vault", "template"]
                    },
                    "vault.settings.quick_fact_templates.order.update": {
                        "uri": "vaults\/{vault}\/settings\/quickFactTemplates\/{template}\/order",
                        "methods": ["PUT"],
                        "parameters": ["vault", "template"]
                    },
                    "vault.settings.quick_fact_templates.destroy": {
                        "uri": "vaults\/{vault}\/settings\/quickFactTemplates\/{template}",
                        "methods": ["DELETE"],
                        "parameters": ["vault", "template"]
                    },
                    "vault.search.index": {
                        "uri": "vaults\/{vault}\/search",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault"]
                    },
                    "vault.search.show": {
                        "uri": "vaults\/{vault}\/search",
                        "methods": ["POST"],
                        "parameters": ["vault"]
                    },
                    "vault.user.search.mostconsulted": {
                        "uri": "vaults\/{vault}\/search\/user\/contact\/mostConsulted",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["vault"]
                    },
                    "vault.user.search.index": {
                        "uri": "vaults\/{vault}\/search\/user\/contacts",
                        "methods": ["POST"],
                        "parameters": ["vault"]
                    },
                    "settings.index": {
                        "uri": "settings",
                        "methods": ["GET", "HEAD"]
                    },
                    "settings.preferences.index": {
                        "uri": "settings\/preferences",
                        "methods": ["GET", "HEAD"]
                    },
                    "settings.preferences.name.store": {
                        "uri": "settings\/preferences\/name",
                        "methods": ["POST"]
                    },
                    "settings.preferences.date.store": {
                        "uri": "settings\/preferences\/date",
                        "methods": ["POST"]
                    },
                    "settings.preferences.timezone.store": {
                        "uri": "settings\/preferences\/timezone",
                        "methods": ["POST"]
                    },
                    "settings.preferences.number.store": {
                        "uri": "settings\/preferences\/number",
                        "methods": ["POST"]
                    },
                    "settings.preferences.distance.store": {
                        "uri": "settings\/preferences\/distance",
                        "methods": ["POST"]
                    },
                    "settings.preferences.maps.store": {
                        "uri": "settings\/preferences\/maps",
                        "methods": ["POST"]
                    },
                    "settings.preferences.locale.store": {
                        "uri": "settings\/preferences\/locale",
                        "methods": ["POST"]
                    },
                    "settings.preferences.help.store": {
                        "uri": "settings\/preferences\/help",
                        "methods": ["POST"]
                    },
                    "settings.notifications.index": {
                        "uri": "settings\/notifications",
                        "methods": ["GET", "HEAD"]
                    },
                    "settings.notifications.store": {
                        "uri": "settings\/notifications",
                        "methods": ["POST"]
                    },
                    "settings.notifications.telegram.store": {
                        "uri": "settings\/notifications\/telegram",
                        "methods": ["POST"]
                    },
                    "settings.notifications.verification.store": {
                        "uri": "settings\/notifications\/{notification}\/verify\/{uuid}",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["notification", "uuid"]
                    },
                    "settings.notifications.test.store": {
                        "uri": "settings\/notifications\/{notification}\/test",
                        "methods": ["POST"],
                        "parameters": ["notification"]
                    },
                    "settings.notifications.toggle.update": {
                        "uri": "settings\/notifications\/{notification}\/toggle",
                        "methods": ["PUT"],
                        "parameters": ["notification"]
                    },
                    "settings.notifications.destroy": {
                        "uri": "settings\/notifications\/{notification}",
                        "methods": ["DELETE"],
                        "parameters": ["notification"]
                    },
                    "settings.notifications.log.index": {
                        "uri": "settings\/notifications\/{notification}\/logs",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["notification"]
                    },
                    "settings.user.index": {
                        "uri": "settings\/users",
                        "methods": ["GET", "HEAD"]
                    },
                    "settings.user.create": {
                        "uri": "settings\/users\/create",
                        "methods": ["GET", "HEAD"]
                    },
                    "settings.user.store": {
                        "uri": "settings\/users",
                        "methods": ["POST"]
                    },
                    "settings.user.show": {
                        "uri": "settings\/users\/{user}",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["user"]
                    },
                    "settings.user.update": {
                        "uri": "settings\/users\/{user}",
                        "methods": ["PUT"],
                        "parameters": ["user"]
                    },
                    "settings.user.destroy": {
                        "uri": "settings\/users\/{user}",
                        "methods": ["DELETE"],
                        "parameters": ["user"]
                    },
                    "settings.personalize.index": {
                        "uri": "settings\/personalize",
                        "methods": ["GET", "HEAD"]
                    },
                    "settings.personalize.relationship.index": {
                        "uri": "settings\/personalize\/relationships",
                        "methods": ["GET", "HEAD"]
                    },
                    "settings.personalize.relationship.grouptype.store": {
                        "uri": "settings\/personalize\/relationships",
                        "methods": ["POST"]
                    },
                    "settings.personalize.relationship.grouptype.update": {
                        "uri": "settings\/personalize\/relationships\/{groupType}",
                        "methods": ["PUT"],
                        "parameters": ["groupType"]
                    },
                    "settings.personalize.relationship.grouptype.destroy": {
                        "uri": "settings\/personalize\/relationships\/{groupType}",
                        "methods": ["DELETE"],
                        "parameters": ["groupType"]
                    },
                    "settings.personalize.relationship.type.store": {
                        "uri": "settings\/personalize\/relationships\/{groupType}\/types",
                        "methods": ["POST"],
                        "parameters": ["groupType"]
                    },
                    "settings.personalize.relationship.type.update": {
                        "uri": "settings\/personalize\/relationships\/{groupType}\/types\/{type}",
                        "methods": ["PUT"],
                        "parameters": ["groupType", "type"]
                    },
                    "settings.personalize.relationship.type.destroy": {
                        "uri": "settings\/personalize\/relationships\/{groupType}\/types\/{type}",
                        "methods": ["DELETE"],
                        "parameters": ["groupType", "type"]
                    },
                    "settings.personalize.call_reasons.index": {
                        "uri": "settings\/personalize\/callReasonTypes",
                        "methods": ["GET", "HEAD"]
                    },
                    "settings.personalize.call_reasons.type.store": {
                        "uri": "settings\/personalize\/callReasonTypes",
                        "methods": ["POST"]
                    },
                    "settings.personalize.call_reasons.type.update": {
                        "uri": "settings\/personalize\/callReasonTypes\/{callReasonType}",
                        "methods": ["PUT"],
                        "parameters": ["callReasonType"]
                    },
                    "settings.personalize.call_reasons.type.destroy": {
                        "uri": "settings\/personalize\/callReasonTypes\/{callReasonType}",
                        "methods": ["DELETE"],
                        "parameters": ["callReasonType"]
                    },
                    "settings.personalize.call_reasons.store": {
                        "uri": "settings\/personalize\/callReasonTypes\/{callReasonType}\/reasons",
                        "methods": ["POST"],
                        "parameters": ["callReasonType"]
                    },
                    "settings.personalize.call_reasons.update": {
                        "uri": "settings\/personalize\/callReasonTypes\/{callReasonType}\/reasons\/{reason}",
                        "methods": ["PUT"],
                        "parameters": ["callReasonType", "reason"]
                    },
                    "settings.personalize.call_reasons.destroy": {
                        "uri": "settings\/personalize\/callReasonTypes\/{callReasonType}\/reasons\/{reason}",
                        "methods": ["DELETE"],
                        "parameters": ["callReasonType", "reason"]
                    },
                    "settings.personalize.gift_occasions.index": {
                        "uri": "settings\/personalize\/giftOccasions",
                        "methods": ["GET", "HEAD"]
                    },
                    "settings.personalize.gift_occasions.store": {
                        "uri": "settings\/personalize\/giftOccasions",
                        "methods": ["POST"]
                    },
                    "settings.personalize.gift_occasions.update": {
                        "uri": "settings\/personalize\/giftOccasions\/{giftOccasion}",
                        "methods": ["PUT"],
                        "parameters": ["giftOccasion"]
                    },
                    "settings.personalize.gift_occasions.destroy": {
                        "uri": "settings\/personalize\/giftOccasions\/{giftOccasion}",
                        "methods": ["DELETE"],
                        "parameters": ["giftOccasion"]
                    },
                    "settings.personalize.gift_occasions.order.update": {
                        "uri": "settings\/personalize\/giftOccasions\/{giftOccasion}\/position",
                        "methods": ["POST"],
                        "parameters": ["giftOccasion"]
                    },
                    "settings.personalize.gift_states.index": {
                        "uri": "settings\/personalize\/giftStates",
                        "methods": ["GET", "HEAD"]
                    },
                    "settings.personalize.gift_states.store": {
                        "uri": "settings\/personalize\/giftStates",
                        "methods": ["POST"]
                    },
                    "settings.personalize.gift_states.update": {
                        "uri": "settings\/personalize\/giftStates\/{giftState}",
                        "methods": ["PUT"],
                        "parameters": ["giftState"]
                    },
                    "settings.personalize.gift_states.destroy": {
                        "uri": "settings\/personalize\/giftStates\/{giftState}",
                        "methods": ["DELETE"],
                        "parameters": ["giftState"]
                    },
                    "settings.personalize.gift_states.order.update": {
                        "uri": "settings\/personalize\/giftStates\/{giftState}\/position",
                        "methods": ["POST"],
                        "parameters": ["giftState"]
                    },
                    "settings.personalize.post_templates.index": {
                        "uri": "settings\/personalize\/postTemplates",
                        "methods": ["GET", "HEAD"]
                    },
                    "settings.personalize.post_templates.store": {
                        "uri": "settings\/personalize\/postTemplates",
                        "methods": ["POST"]
                    },
                    "settings.personalize.post_templates.update": {
                        "uri": "settings\/personalize\/postTemplates\/{postTemplate}",
                        "methods": ["PUT"],
                        "parameters": ["postTemplate"]
                    },
                    "settings.personalize.post_templates.destroy": {
                        "uri": "settings\/personalize\/postTemplates\/{postTemplate}",
                        "methods": ["DELETE"],
                        "parameters": ["postTemplate"]
                    },
                    "settings.personalize.post_templates.order.update": {
                        "uri": "settings\/personalize\/postTemplates\/{postTemplate}\/position",
                        "methods": ["POST"],
                        "parameters": ["postTemplate"]
                    },
                    "settings.personalize.post_templates.section.store": {
                        "uri": "settings\/personalize\/postTemplates\/{postTemplate}\/sections",
                        "methods": ["POST"],
                        "parameters": ["postTemplate"]
                    },
                    "settings.personalize.post_templates.section.update": {
                        "uri": "settings\/personalize\/postTemplates\/{postTemplate}\/sections\/{section}",
                        "methods": ["PUT"],
                        "parameters": ["postTemplate", "section"]
                    },
                    "settings.personalize.post_templates.section.destroy": {
                        "uri": "settings\/personalize\/postTemplates\/{postTemplate}\/sections\/{section}",
                        "methods": ["DELETE"],
                        "parameters": ["postTemplate", "section"]
                    },
                    "settings.personalize.post_templates.section.order.update": {
                        "uri": "settings\/personalize\/postTemplates\/{postTemplate}\/sections\/{section}\/position",
                        "methods": ["POST"],
                        "parameters": ["postTemplate", "section"]
                    },
                    "settings.personalize.group_types.index": {
                        "uri": "settings\/personalize\/groupTypes",
                        "methods": ["GET", "HEAD"]
                    },
                    "settings.personalize.group_types.store": {
                        "uri": "settings\/personalize\/groupTypes",
                        "methods": ["POST"]
                    },
                    "settings.personalize.group_types.update": {
                        "uri": "settings\/personalize\/groupTypes\/{type}",
                        "methods": ["PUT"],
                        "parameters": ["type"]
                    },
                    "settings.personalize.group_types.destroy": {
                        "uri": "settings\/personalize\/groupTypes\/{type}",
                        "methods": ["DELETE"],
                        "parameters": ["type"]
                    },
                    "settings.personalize.group_types.order.update": {
                        "uri": "settings\/personalize\/groupTypes\/{type}\/position",
                        "methods": ["POST"],
                        "parameters": ["type"]
                    },
                    "settings.personalize.group_types.roles.store": {
                        "uri": "settings\/personalize\/groupTypes\/{type}\/groupTypeRoles",
                        "methods": ["POST"],
                        "parameters": ["type"]
                    },
                    "settings.personalize.group_types.roles.update": {
                        "uri": "settings\/personalize\/groupTypes\/{type}\/groupTypeRoles\/{role}",
                        "methods": ["PUT"],
                        "parameters": ["type", "role"]
                    },
                    "settings.personalize.group_types.roles.destroy": {
                        "uri": "settings\/personalize\/groupTypes\/{type}\/groupTypeRoles\/{role}",
                        "methods": ["DELETE"],
                        "parameters": ["type", "role"]
                    },
                    "settings.personalize.group_types.roles.order.update": {
                        "uri": "settings\/personalize\/groupTypes\/{type}\/groupTypeRoles\/{role}\/position",
                        "methods": ["POST"],
                        "parameters": ["type", "role"]
                    },
                    "settings.personalize.gender.index": {
                        "uri": "settings\/personalize\/genders",
                        "methods": ["GET", "HEAD"]
                    },
                    "settings.personalize.gender.store": {
                        "uri": "settings\/personalize\/genders",
                        "methods": ["POST"]
                    },
                    "settings.personalize.gender.update": {
                        "uri": "settings\/personalize\/genders\/{gender}",
                        "methods": ["PUT"],
                        "parameters": ["gender"]
                    },
                    "settings.personalize.gender.destroy": {
                        "uri": "settings\/personalize\/genders\/{gender}",
                        "methods": ["DELETE"],
                        "parameters": ["gender"]
                    },
                    "settings.personalize.pronoun.index": {
                        "uri": "settings\/personalize\/pronouns",
                        "methods": ["GET", "HEAD"]
                    },
                    "settings.personalize.pronoun.store": {
                        "uri": "settings\/personalize\/pronouns",
                        "methods": ["POST"]
                    },
                    "settings.personalize.pronoun.update": {
                        "uri": "settings\/personalize\/pronouns\/{pronoun}",
                        "methods": ["PUT"],
                        "parameters": ["pronoun"]
                    },
                    "settings.personalize.pronoun.destroy": {
                        "uri": "settings\/personalize\/pronouns\/{pronoun}",
                        "methods": ["DELETE"],
                        "parameters": ["pronoun"]
                    },
                    "settings.personalize.address_type.index": {
                        "uri": "settings\/personalize\/addressTypes",
                        "methods": ["GET", "HEAD"]
                    },
                    "settings.personalize.address_type.store": {
                        "uri": "settings\/personalize\/addressTypes",
                        "methods": ["POST"]
                    },
                    "settings.personalize.address_type.update": {
                        "uri": "settings\/personalize\/addressTypes\/{addressType}",
                        "methods": ["PUT"],
                        "parameters": ["addressType"]
                    },
                    "settings.personalize.address_type.destroy": {
                        "uri": "settings\/personalize\/addressTypes\/{addressType}",
                        "methods": ["DELETE"],
                        "parameters": ["addressType"]
                    },
                    "settings.personalize.pet_category.index": {
                        "uri": "settings\/personalize\/petCategories",
                        "methods": ["GET", "HEAD"]
                    },
                    "settings.personalize.pet_category.store": {
                        "uri": "settings\/personalize\/petCategories",
                        "methods": ["POST"]
                    },
                    "settings.personalize.pet_category.update": {
                        "uri": "settings\/personalize\/petCategories\/{petCategory}",
                        "methods": ["PUT"],
                        "parameters": ["petCategory"]
                    },
                    "settings.personalize.pet_category.destroy": {
                        "uri": "settings\/personalize\/petCategories\/{petCategory}",
                        "methods": ["DELETE"],
                        "parameters": ["petCategory"]
                    },
                    "settings.personalize.contact_information_type.index": {
                        "uri": "settings\/personalize\/contactInformationType",
                        "methods": ["GET", "HEAD"]
                    },
                    "settings.personalize.contact_information_type.store": {
                        "uri": "settings\/personalize\/contactInformationType",
                        "methods": ["POST"]
                    },
                    "settings.personalize.contact_information_type.update": {
                        "uri": "settings\/personalize\/contactInformationType\/{type}",
                        "methods": ["PUT"],
                        "parameters": ["type"]
                    },
                    "settings.personalize.contact_information_type.destroy": {
                        "uri": "settings\/personalize\/contactInformationType\/{type}",
                        "methods": ["DELETE"],
                        "parameters": ["type"]
                    },
                    "settings.personalize.template.index": {
                        "uri": "settings\/personalize\/templates",
                        "methods": ["GET", "HEAD"]
                    },
                    "settings.personalize.template.store": {
                        "uri": "settings\/personalize\/templates",
                        "methods": ["POST"]
                    },
                    "settings.personalize.template.update": {
                        "uri": "settings\/personalize\/templates\/{template}",
                        "methods": ["PUT"],
                        "parameters": ["template"]
                    },
                    "settings.personalize.template.destroy": {
                        "uri": "settings\/personalize\/templates\/{template}",
                        "methods": ["DELETE"],
                        "parameters": ["template"]
                    },
                    "settings.personalize.template.show": {
                        "uri": "settings\/personalize\/templates\/{template}",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["template"]
                    },
                    "settings.personalize.template.template_page.store": {
                        "uri": "settings\/personalize\/templates\/{template}",
                        "methods": ["POST"],
                        "parameters": ["template"]
                    },
                    "settings.personalize.template.template_page.update": {
                        "uri": "settings\/personalize\/templates\/{template}\/template_pages\/{page}",
                        "methods": ["PUT"],
                        "parameters": ["template", "page"]
                    },
                    "settings.personalize.template.template_page.destroy": {
                        "uri": "settings\/personalize\/templates\/{template}\/template_pages\/{page}",
                        "methods": ["DELETE"],
                        "parameters": ["template", "page"]
                    },
                    "settings.personalize.template.template_page.show": {
                        "uri": "settings\/personalize\/templates\/{template}\/template_pages\/{page}",
                        "methods": ["GET", "HEAD"],
                        "parameters": ["template", "page"]
                    },
                    "settings.personalize.template.template_page.order.update": {
                        "uri": "settings\/personalize\/templates\/{template}\/template_pages\/{page}\/order",
                        "methods": ["POST"],
                        "parameters": ["template", "page"]
                    },
                    "settings.personalize.template.template_page.module.store": {
                        "uri": "settings\/personalize\/templates\/{template}\/template_pages\/{page}\/modules",
                        "methods": ["POST"],
                        "parameters": ["template", "page"]
                    },
                    "settings.personalize.template.template_page.module.order.update": {
                        "uri": "settings\/personalize\/templates\/{template}\/template_pages\/{page}\/modules\/{module}\/order",
                        "methods": ["POST"],
                        "parameters": ["template", "page", "module"]
                    },
                    "settings.personalize.template.template_page.module.destroy": {
                        "uri": "settings\/personalize\/templates\/{template}\/template_pages\/{page}\/modules\/{module}",
                        "methods": ["DELETE"],
                        "parameters": ["template", "page", "module"]
                    },
                    "settings.personalize.module.index": {
                        "uri": "settings\/personalize\/modules",
                        "methods": ["GET", "HEAD"]
                    },
                    "settings.personalize.module.store": {
                        "uri": "settings\/personalize\/modules",
                        "methods": ["POST"]
                    },
                    "settings.personalize.module.update": {
                        "uri": "settings\/personalize\/modules\/{module}",
                        "methods": ["PUT"],
                        "parameters": ["module"]
                    },
                    "settings.personalize.module.destroy": {
                        "uri": "settings\/personalize\/modules\/{module}",
                        "methods": ["DELETE"],
                        "parameters": ["module"]
                    },
                    "settings.personalize.currency.index": {
                        "uri": "settings\/personalize\/currencies",
                        "methods": ["GET", "HEAD"]
                    },
                    "settings.personalize.currency.update": {
                        "uri": "settings\/personalize\/currencies\/{currency}",
                        "methods": ["PUT"],
                        "parameters": ["currency"]
                    },
                    "settings.personalize.currency.store": {
                        "uri": "settings\/personalize\/currencies",
                        "methods": ["POST"]
                    },
                    "settings.personalize.currency.destroy": {
                        "uri": "settings\/personalize\/currencies",
                        "methods": ["DELETE"]
                    },
                    "settings.personalize.religions.index": {
                        "uri": "settings\/personalize\/religions",
                        "methods": ["GET", "HEAD"]
                    },
                    "settings.personalize.religions.store": {
                        "uri": "settings\/personalize\/religions",
                        "methods": ["POST"]
                    },
                    "settings.personalize.religions.update": {
                        "uri": "settings\/personalize\/religions\/{religion}",
                        "methods": ["PUT"],
                        "parameters": ["religion"]
                    },
                    "settings.personalize.religions.destroy": {
                        "uri": "settings\/personalize\/religions\/{religion}",
                        "methods": ["DELETE"],
                        "parameters": ["religion"]
                    },
                    "settings.personalize.religions.order.update": {
                        "uri": "settings\/personalize\/religions\/{religion}\/position",
                        "methods": ["POST"],
                        "parameters": ["religion"]
                    },
                    "settings.storage.index": {
                        "uri": "settings\/storage",
                        "methods": ["GET", "HEAD"]
                    },
                    "settings.cancel.index": {
                        "uri": "settings\/cancel",
                        "methods": ["GET", "HEAD"]
                    },
                    "settings.cancel.destroy": {
                        "uri": "settings\/cancel",
                        "methods": ["PUT"]
                    },
                    "currencies.index": {
                        "uri": "currencies",
                        "methods": ["GET", "HEAD"]
                    },
                    "provider.delete": {
                        "uri": "auth\/{driver}",
                        "methods": ["DELETE"],
                        "parameters": ["driver"]
                    }
                }
            };
            !function(t, r) {
                "object" == typeof exports && "undefined" != typeof module ? module.exports = r() : "function" == typeof define && define.amd ? define(r) : (t || self).route = r()
            }(this, function() {
                function t(t, r) {
                    for (var n = 0; n < r.length; n++) {
                        var e = r[n];
                        e.enumerable = e.enumerable || !1,
                        e.configurable = !0,
                        "value"in e && (e.writable = !0),
                        Object.defineProperty(t, u(e.key), e)
                    }
                }
                function r(r, n, e) {
                    return n && t(r.prototype, n),
                    e && t(r, e),
                    Object.defineProperty(r, "prototype", {
                        writable: !1
                    }),
                    r
                }
                function n() {
                    return n = Object.assign ? Object.assign.bind() : function(t) {
                        for (var r = 1; r < arguments.length; r++) {
                            var n = arguments[r];
                            for (var e in n)
                                ({}).hasOwnProperty.call(n, e) && (t[e] = n[e])
                        }
                        return t
                    }
                    ,
                    n.apply(null, arguments)
                }
                function e(t) {
                    return e = Object.setPrototypeOf ? Object.getPrototypeOf.bind() : function(t) {
                        return t.__proto__ || Object.getPrototypeOf(t)
                    }
                    ,
                    e(t)
                }
                function o() {
                    try {
                        var t = !Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], function() {}))
                    } catch (t) {}
                    return (o = function() {
                        return !!t
                    }
                    )()
                }
                function i(t, r) {
                    return i = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function(t, r) {
                        return t.__proto__ = r,
                        t
                    }
                    ,
                    i(t, r)
                }
                function u(t) {
                    var r = function(t) {
                        if ("object" != typeof t || !t)
                            return t;
                        var r = t[Symbol.toPrimitive];
                        if (void 0 !== r) {
                            var n = r.call(t, "string");
                            if ("object" != typeof n)
                                return n;
                            throw new TypeError("@@toPrimitive must return a primitive value.")
                        }
                        return String(t)
                    }(t);
                    return "symbol" == typeof r ? r : r + ""
                }
                function f(t) {
                    var r = "function" == typeof Map ? new Map : void 0;
                    return f = function(t) {
                        if (null === t || !function(t) {
                            try {
                                return -1 !== Function.toString.call(t).indexOf("[native code]")
                            } catch (r) {
                                return "function" == typeof t
                            }
                        }(t))
                            return t;
                        if ("function" != typeof t)
                            throw new TypeError("Super expression must either be null or a function");
                        if (void 0 !== r) {
                            if (r.has(t))
                                return r.get(t);
                            r.set(t, n)
                        }
                        function n() {
                            return function(t, r, n) {
                                if (o())
                                    return Reflect.construct.apply(null, arguments);
                                var e = [null];
                                e.push.apply(e, r);
                                var u = new (t.bind.apply(t, e));
                                return n && i(u, n.prototype),
                                u
                            }(t, arguments, e(this).constructor)
                        }
                        return n.prototype = Object.create(t.prototype, {
                            constructor: {
                                value: n,
                                enumerable: !1,
                                writable: !0,
                                configurable: !0
                            }
                        }),
                        i(n, t)
                    }
                    ,
                    f(t)
                }
                var a = String.prototype.replace
                  , c = /%20/g
                  , l = "RFC3986"
                  , s = {
                    default: l,
                    formatters: {
                        RFC1738: function(t) {
                            return a.call(t, c, "+")
                        },
                        RFC3986: function(t) {
                            return String(t)
                        }
                    },
                    RFC1738: "RFC1738",
                    RFC3986: l
                }
                  , v = Object.prototype.hasOwnProperty
                  , p = Array.isArray
                  , y = function() {
                    for (var t = [], r = 0; r < 256; ++r)
                        t.push("%" + ((r < 16 ? "0" : "") + r.toString(16)).toUpperCase());
                    return t
                }()
                  , d = function(t, r) {
                    for (var n = r && r.plainObjects ? Object.create(null) : {}, e = 0; e < t.length; ++e)
                        void 0 !== t[e] && (n[e] = t[e]);
                    return n
                }
                  , b = {
                    arrayToObject: d,
                    assign: function(t, r) {
                        return Object.keys(r).reduce(function(t, n) {
                            return t[n] = r[n],
                            t
                        }, t)
                    },
                    combine: function(t, r) {
                        return [].concat(t, r)
                    },
                    compact: function(t) {
                        for (var r = [{
                            obj: {
                                o: t
                            },
                            prop: "o"
                        }], n = [], e = 0; e < r.length; ++e)
                            for (var o = r[e], i = o.obj[o.prop], u = Object.keys(i), f = 0; f < u.length; ++f) {
                                var a = u[f]
                                  , c = i[a];
                                "object" == typeof c && null !== c && -1 === n.indexOf(c) && (r.push({
                                    obj: i,
                                    prop: a
                                }),
                                n.push(c))
                            }
                        return function(t) {
                            for (; t.length > 1; ) {
                                var r = t.pop()
                                  , n = r.obj[r.prop];
                                if (p(n)) {
                                    for (var e = [], o = 0; o < n.length; ++o)
                                        void 0 !== n[o] && e.push(n[o]);
                                    r.obj[r.prop] = e
                                }
                            }
                        }(r),
                        t
                    },
                    decode: function(t, r, n) {
                        var e = t.replace(/\+/g, " ");
                        if ("iso-8859-1" === n)
                            return e.replace(/%[0-9a-f]{2}/gi, unescape);
                        try {
                            return decodeURIComponent(e)
                        } catch (t) {
                            return e
                        }
                    },
                    encode: function(t, r, n, e, o) {
                        if (0 === t.length)
                            return t;
                        var i = t;
                        if ("symbol" == typeof t ? i = Symbol.prototype.toString.call(t) : "string" != typeof t && (i = String(t)),
                        "iso-8859-1" === n)
                            return escape(i).replace(/%u[0-9a-f]{4}/gi, function(t) {
                                return "%26%23" + parseInt(t.slice(2), 16) + "%3B"
                            });
                        for (var u = "", f = 0; f < i.length; ++f) {
                            var a = i.charCodeAt(f);
                            45 === a || 46 === a || 95 === a || 126 === a || a >= 48 && a <= 57 || a >= 65 && a <= 90 || a >= 97 && a <= 122 || o === s.RFC1738 && (40 === a || 41 === a) ? u += i.charAt(f) : a < 128 ? u += y[a] : a < 2048 ? u += y[192 | a >> 6] + y[128 | 63 & a] : a < 55296 || a >= 57344 ? u += y[224 | a >> 12] + y[128 | a >> 6 & 63] + y[128 | 63 & a] : (a = 65536 + ((1023 & a) << 10 | 1023 & i.charCodeAt(f += 1)),
                            u += y[240 | a >> 18] + y[128 | a >> 12 & 63] + y[128 | a >> 6 & 63] + y[128 | 63 & a])
                        }
                        return u
                    },
                    isBuffer: function(t) {
                        return !(!t || "object" != typeof t || !(t.constructor && t.constructor.isBuffer && t.constructor.isBuffer(t)))
                    },
                    isRegExp: function(t) {
                        return "[object RegExp]" === Object.prototype.toString.call(t)
                    },
                    maybeMap: function(t, r) {
                        if (p(t)) {
                            for (var n = [], e = 0; e < t.length; e += 1)
                                n.push(r(t[e]));
                            return n
                        }
                        return r(t)
                    },
                    merge: function t(r, n, e) {
                        if (!n)
                            return r;
                        if ("object" != typeof n) {
                            if (p(r))
                                r.push(n);
                            else {
                                if (!r || "object" != typeof r)
                                    return [r, n];
                                (e && (e.plainObjects || e.allowPrototypes) || !v.call(Object.prototype, n)) && (r[n] = !0)
                            }
                            return r
                        }
                        if (!r || "object" != typeof r)
                            return [r].concat(n);
                        var o = r;
                        return p(r) && !p(n) && (o = d(r, e)),
                        p(r) && p(n) ? (n.forEach(function(n, o) {
                            if (v.call(r, o)) {
                                var i = r[o];
                                i && "object" == typeof i && n && "object" == typeof n ? r[o] = t(i, n, e) : r.push(n)
                            } else
                                r[o] = n
                        }),
                        r) : Object.keys(n).reduce(function(r, o) {
                            var i = n[o];
                            return r[o] = v.call(r, o) ? t(r[o], i, e) : i,
                            r
                        }, o)
                    }
                }
                  , h = Object.prototype.hasOwnProperty
                  , g = {
                    brackets: function(t) {
                        return t + "[]"
                    },
                    comma: "comma",
                    indices: function(t, r) {
                        return t + "[" + r + "]"
                    },
                    repeat: function(t) {
                        return t
                    }
                }
                  , m = Array.isArray
                  , j = String.prototype.split
                  , w = Array.prototype.push
                  , O = function(t, r) {
                    w.apply(t, m(r) ? r : [r])
                }
                  , E = Date.prototype.toISOString
                  , R = s.default
                  , S = {
                    addQueryPrefix: !1,
                    allowDots: !1,
                    charset: "utf-8",
                    charsetSentinel: !1,
                    delimiter: "&",
                    encode: !0,
                    encoder: b.encode,
                    encodeValuesOnly: !1,
                    format: R,
                    formatter: s.formatters[R],
                    indices: !1,
                    serializeDate: function(t) {
                        return E.call(t)
                    },
                    skipNulls: !1,
                    strictNullHandling: !1
                }
                  , k = function t(r, n, e, o, i, u, f, a, c, l, s, v, p, y) {
                    var d, h = r;
                    if ("function" == typeof f ? h = f(n, h) : h instanceof Date ? h = l(h) : "comma" === e && m(h) && (h = b.maybeMap(h, function(t) {
                        return t instanceof Date ? l(t) : t
                    })),
                    null === h) {
                        if (o)
                            return u && !p ? u(n, S.encoder, y, "key", s) : n;
                        h = ""
                    }
                    if ("string" == typeof (d = h) || "number" == typeof d || "boolean" == typeof d || "symbol" == typeof d || "bigint" == typeof d || b.isBuffer(h)) {
                        if (u) {
                            var g = p ? n : u(n, S.encoder, y, "key", s);
                            if ("comma" === e && p) {
                                for (var w = j.call(String(h), ","), E = "", R = 0; R < w.length; ++R)
                                    E += (0 === R ? "" : ",") + v(u(w[R], S.encoder, y, "value", s));
                                return [v(g) + "=" + E]
                            }
                            return [v(g) + "=" + v(u(h, S.encoder, y, "value", s))]
                        }
                        return [v(n) + "=" + v(String(h))]
                    }
                    var k, T = [];
                    if (void 0 === h)
                        return T;
                    if ("comma" === e && m(h))
                        k = [{
                            value: h.length > 0 ? h.join(",") || null : void 0
                        }];
                    else if (m(f))
                        k = f;
                    else {
                        var $ = Object.keys(h);
                        k = a ? $.sort(a) : $
                    }
                    for (var x = 0; x < k.length; ++x) {
                        var N = k[x]
                          , C = "object" == typeof N && void 0 !== N.value ? N.value : h[N];
                        if (!i || null !== C) {
                            var A = m(h) ? "function" == typeof e ? e(n, N) : n : n + (c ? "." + N : "[" + N + "]");
                            O(T, t(C, A, e, o, i, u, f, a, c, l, s, v, p, y))
                        }
                    }
                    return T
                }
                  , T = Object.prototype.hasOwnProperty
                  , $ = Array.isArray
                  , x = {
                    allowDots: !1,
                    allowPrototypes: !1,
                    arrayLimit: 20,
                    charset: "utf-8",
                    charsetSentinel: !1,
                    comma: !1,
                    decoder: b.decode,
                    delimiter: "&",
                    depth: 5,
                    ignoreQueryPrefix: !1,
                    interpretNumericEntities: !1,
                    parameterLimit: 1e3,
                    parseArrays: !0,
                    plainObjects: !1,
                    strictNullHandling: !1
                }
                  , N = function(t) {
                    return t.replace(/&#(\d+);/g, function(t, r) {
                        return String.fromCharCode(parseInt(r, 10))
                    })
                }
                  , C = function(t, r) {
                    return t && "string" == typeof t && r.comma && t.indexOf(",") > -1 ? t.split(",") : t
                }
                  , A = function(t, r, n, e) {
                    if (t) {
                        var o = n.allowDots ? t.replace(/\.([^.[]+)/g, "[$1]") : t
                          , i = /(\[[^[\]]*])/g
                          , u = n.depth > 0 && /(\[[^[\]]*])/.exec(o)
                          , f = u ? o.slice(0, u.index) : o
                          , a = [];
                        if (f) {
                            if (!n.plainObjects && T.call(Object.prototype, f) && !n.allowPrototypes)
                                return;
                            a.push(f)
                        }
                        for (var c = 0; n.depth > 0 && null !== (u = i.exec(o)) && c < n.depth; ) {
                            if (c += 1,
                            !n.plainObjects && T.call(Object.prototype, u[1].slice(1, -1)) && !n.allowPrototypes)
                                return;
                            a.push(u[1])
                        }
                        return u && a.push("[" + o.slice(u.index) + "]"),
                        function(t, r, n, e) {
                            for (var o = e ? r : C(r, n), i = t.length - 1; i >= 0; --i) {
                                var u, f = t[i];
                                if ("[]" === f && n.parseArrays)
                                    u = [].concat(o);
                                else {
                                    u = n.plainObjects ? Object.create(null) : {};
                                    var a = "[" === f.charAt(0) && "]" === f.charAt(f.length - 1) ? f.slice(1, -1) : f
                                      , c = parseInt(a, 10);
                                    n.parseArrays || "" !== a ? !isNaN(c) && f !== a && String(c) === a && c >= 0 && n.parseArrays && c <= n.arrayLimit ? (u = [])[c] = o : "__proto__" !== a && (u[a] = o) : u = {
                                        0: o
                                    }
                                }
                                o = u
                            }
                            return o
                        }(a, r, n, e)
                    }
                }
                  , D = function(t, r) {
                    var n = function(t) {
                        if (!t)
                            return x;
                        if (null != t.decoder && "function" != typeof t.decoder)
                            throw new TypeError("Decoder has to be a function.");
                        if (void 0 !== t.charset && "utf-8" !== t.charset && "iso-8859-1" !== t.charset)
                            throw new TypeError("The charset option must be either utf-8, iso-8859-1, or undefined");
                        return {
                            allowDots: void 0 === t.allowDots ? x.allowDots : !!t.allowDots,
                            allowPrototypes: "boolean" == typeof t.allowPrototypes ? t.allowPrototypes : x.allowPrototypes,
                            arrayLimit: "number" == typeof t.arrayLimit ? t.arrayLimit : x.arrayLimit,
                            charset: void 0 === t.charset ? x.charset : t.charset,
                            charsetSentinel: "boolean" == typeof t.charsetSentinel ? t.charsetSentinel : x.charsetSentinel,
                            comma: "boolean" == typeof t.comma ? t.comma : x.comma,
                            decoder: "function" == typeof t.decoder ? t.decoder : x.decoder,
                            delimiter: "string" == typeof t.delimiter || b.isRegExp(t.delimiter) ? t.delimiter : x.delimiter,
                            depth: "number" == typeof t.depth || !1 === t.depth ? +t.depth : x.depth,
                            ignoreQueryPrefix: !0 === t.ignoreQueryPrefix,
                            interpretNumericEntities: "boolean" == typeof t.interpretNumericEntities ? t.interpretNumericEntities : x.interpretNumericEntities,
                            parameterLimit: "number" == typeof t.parameterLimit ? t.parameterLimit : x.parameterLimit,
                            parseArrays: !1 !== t.parseArrays,
                            plainObjects: "boolean" == typeof t.plainObjects ? t.plainObjects : x.plainObjects,
                            strictNullHandling: "boolean" == typeof t.strictNullHandling ? t.strictNullHandling : x.strictNullHandling
                        }
                    }(r);
                    if ("" === t || null == t)
                        return n.plainObjects ? Object.create(null) : {};
                    for (var e = "string" == typeof t ? function(t, r) {
                        var n, e = {}, o = (r.ignoreQueryPrefix ? t.replace(/^\?/, "") : t).split(r.delimiter, Infinity === r.parameterLimit ? void 0 : r.parameterLimit), i = -1, u = r.charset;
                        if (r.charsetSentinel)
                            for (n = 0; n < o.length; ++n)
                                0 === o[n].indexOf("utf8=") && ("utf8=%E2%9C%93" === o[n] ? u = "utf-8" : "utf8=%26%2310003%3B" === o[n] && (u = "iso-8859-1"),
                                i = n,
                                n = o.length);
                        for (n = 0; n < o.length; ++n)
                            if (n !== i) {
                                var f, a, c = o[n], l = c.indexOf("]="), s = -1 === l ? c.indexOf("=") : l + 1;
                                -1 === s ? (f = r.decoder(c, x.decoder, u, "key"),
                                a = r.strictNullHandling ? null : "") : (f = r.decoder(c.slice(0, s), x.decoder, u, "key"),
                                a = b.maybeMap(C(c.slice(s + 1), r), function(t) {
                                    return r.decoder(t, x.decoder, u, "value")
                                })),
                                a && r.interpretNumericEntities && "iso-8859-1" === u && (a = N(a)),
                                c.indexOf("[]=") > -1 && (a = $(a) ? [a] : a),
                                e[f] = T.call(e, f) ? b.combine(e[f], a) : a
                            }
                        return e
                    }(t, n) : t, o = n.plainObjects ? Object.create(null) : {}, i = Object.keys(e), u = 0; u < i.length; ++u) {
                        var f = i[u]
                          , a = A(f, e[f], n, "string" == typeof t);
                        o = b.merge(o, a, n)
                    }
                    return b.compact(o)
                }
                  , P = /*#__PURE__*/
                function() {
                    function t(t, r, n) {
                        var e, o;
                        this.name = t,
                        this.definition = r,
                        this.bindings = null != (e = r.bindings) ? e : {},
                        this.wheres = null != (o = r.wheres) ? o : {},
                        this.config = n
                    }
                    var n = t.prototype;
                    return n.matchesUrl = function(t) {
                        var r, n = this;
                        if (!this.definition.methods.includes("GET"))
                            return !1;
                        var e = this.template.replace(/[.*+$()[\]]/g, "\\$&").replace(/(\/?){([^}?]*)(\??)}/g, function(t, r, e, o) {
                            var i, u = "(?<" + e + ">" + ((null == (i = n.wheres[e]) ? void 0 : i.replace(/(^\^)|(\$$)/g, "")) || "[^/?]+") + ")";
                            return o ? "(" + r + u + ")?" : "" + r + u
                        }).replace(/^\w+:\/\//, "")
                          , o = t.replace(/^\w+:\/\//, "").split("?")
                          , i = o[0]
                          , u = o[1]
                          , f = null != (r = new RegExp("^" + e + "/?$").exec(i)) ? r : new RegExp("^" + e + "/?$").exec(decodeURI(i));
                        if (f) {
                            for (var a in f.groups)
                                f.groups[a] = "string" == typeof f.groups[a] ? decodeURIComponent(f.groups[a]) : f.groups[a];
                            return {
                                params: f.groups,
                                query: D(u)
                            }
                        }
                        return !1
                    }
                    ,
                    n.compile = function(t) {
                        var r = this;
                        return this.parameterSegments.length ? this.template.replace(/{([^}?]+)(\??)}/g, function(n, e, o) {
                            var i, u;
                            if (!o && [null, void 0].includes(t[e]))
                                throw new Error("Ziggy error: '" + e + "' parameter is required for route '" + r.name + "'.");
                            if (r.wheres[e] && !new RegExp("^" + (o ? "(" + r.wheres[e] + ")?" : r.wheres[e]) + "$").test(null != (u = t[e]) ? u : ""))
                                throw new Error("Ziggy error: '" + e + "' parameter '" + t[e] + "' does not match required format '" + r.wheres[e] + "' for route '" + r.name + "'.");
                            return encodeURI(null != (i = t[e]) ? i : "").replace(/%7C/g, "|").replace(/%25/g, "%").replace(/\$/g, "%24")
                        }).replace(this.config.absolute ? /(\.[^/]+?)(\/\/)/ : /(^)(\/\/)/, "$1/").replace(/\/+$/, "") : this.template
                    }
                    ,
                    r(t, [{
                        key: "template",
                        get: function() {
                            var t = (this.origin + "/" + this.definition.uri).replace(/\/+$/, "");
                            return "" === t ? "/" : t
                        }
                    }, {
                        key: "origin",
                        get: function() {
                            return this.config.absolute ? this.definition.domain ? "" + this.config.url.match(/^\w+:\/\//)[0] + this.definition.domain + (this.config.port ? ":" + this.config.port : "") : this.config.url : ""
                        }
                    }, {
                        key: "parameterSegments",
                        get: function() {
                            var t, r;
                            return null != (t = null == (r = this.template.match(/{[^}?]+\??}/g)) ? void 0 : r.map(function(t) {
                                return {
                                    name: t.replace(/{|\??}/g, ""),
                                    required: !/\?}$/.test(t)
                                }
                            })) ? t : []
                        }
                    }])
                }()
                  , F = /*#__PURE__*/
                function(t) {
                    function e(r, e, o, i) {
                        var u;
                        if (void 0 === o && (o = !0),
                        (u = t.call(this) || this).t = null != i ? i : "undefined" != typeof Ziggy ? Ziggy : null == globalThis ? void 0 : globalThis.Ziggy,
                        u.t = n({}, u.t, {
                            absolute: o
                        }),
                        r) {
                            if (!u.t.routes[r])
                                throw new Error("Ziggy error: route '" + r + "' is not in the route list.");
                            u.i = new P(r,u.t.routes[r],u.t),
                            u.u = u.l(e)
                        }
                        return u
                    }
                    var o, u;
                    u = t,
                    (o = e).prototype = Object.create(u.prototype),
                    o.prototype.constructor = o,
                    i(o, u);
                    var f = e.prototype;
                    return f.toString = function() {
                        var t = this
                          , r = Object.keys(this.u).filter(function(r) {
                            return !t.i.parameterSegments.some(function(t) {
                                return t.name === r
                            })
                        }).filter(function(t) {
                            return "_query" !== t
                        }).reduce(function(r, e) {
                            var o;
                            return n({}, r, ((o = {})[e] = t.u[e],
                            o))
                        }, {});
                        return this.i.compile(this.u) + function(t, r) {
                            var n, e = t, o = function(t) {
                                if (!t)
                                    return S;
                                if (null != t.encoder && "function" != typeof t.encoder)
                                    throw new TypeError("Encoder has to be a function.");
                                var r = t.charset || S.charset;
                                if (void 0 !== t.charset && "utf-8" !== t.charset && "iso-8859-1" !== t.charset)
                                    throw new TypeError("The charset option must be either utf-8, iso-8859-1, or undefined");
                                var n = s.default;
                                if (void 0 !== t.format) {
                                    if (!h.call(s.formatters, t.format))
                                        throw new TypeError("Unknown format option provided.");
                                    n = t.format
                                }
                                var e = s.formatters[n]
                                  , o = S.filter;
                                return ("function" == typeof t.filter || m(t.filter)) && (o = t.filter),
                                {
                                    addQueryPrefix: "boolean" == typeof t.addQueryPrefix ? t.addQueryPrefix : S.addQueryPrefix,
                                    allowDots: void 0 === t.allowDots ? S.allowDots : !!t.allowDots,
                                    charset: r,
                                    charsetSentinel: "boolean" == typeof t.charsetSentinel ? t.charsetSentinel : S.charsetSentinel,
                                    delimiter: void 0 === t.delimiter ? S.delimiter : t.delimiter,
                                    encode: "boolean" == typeof t.encode ? t.encode : S.encode,
                                    encoder: "function" == typeof t.encoder ? t.encoder : S.encoder,
                                    encodeValuesOnly: "boolean" == typeof t.encodeValuesOnly ? t.encodeValuesOnly : S.encodeValuesOnly,
                                    filter: o,
                                    format: n,
                                    formatter: e,
                                    serializeDate: "function" == typeof t.serializeDate ? t.serializeDate : S.serializeDate,
                                    skipNulls: "boolean" == typeof t.skipNulls ? t.skipNulls : S.skipNulls,
                                    sort: "function" == typeof t.sort ? t.sort : null,
                                    strictNullHandling: "boolean" == typeof t.strictNullHandling ? t.strictNullHandling : S.strictNullHandling
                                }
                            }(r);
                            "function" == typeof o.filter ? e = (0,
                            o.filter)("", e) : m(o.filter) && (n = o.filter);
                            var i = [];
                            if ("object" != typeof e || null === e)
                                return "";
                            var u = g[r && r.arrayFormat in g ? r.arrayFormat : r && "indices"in r ? r.indices ? "indices" : "repeat" : "indices"];
                            n || (n = Object.keys(e)),
                            o.sort && n.sort(o.sort);
                            for (var f = 0; f < n.length; ++f) {
                                var a = n[f];
                                o.skipNulls && null === e[a] || O(i, k(e[a], a, u, o.strictNullHandling, o.skipNulls, o.encode ? o.encoder : null, o.filter, o.sort, o.allowDots, o.serializeDate, o.format, o.formatter, o.encodeValuesOnly, o.charset))
                            }
                            var c = i.join(o.delimiter)
                              , l = !0 === o.addQueryPrefix ? "?" : "";
                            return o.charsetSentinel && (l += "iso-8859-1" === o.charset ? "utf8=%26%2310003%3B&" : "utf8=%E2%9C%93&"),
                            c.length > 0 ? l + c : ""
                        }(n({}, r, this.u._query), {
                            addQueryPrefix: !0,
                            arrayFormat: "indices",
                            encodeValuesOnly: !0,
                            skipNulls: !0,
                            encoder: function(t, r) {
                                return "boolean" == typeof t ? Number(t) : r(t)
                            }
                        })
                    }
                    ,
                    f.v = function(t) {
                        var r = this;
                        t ? this.t.absolute && t.startsWith("/") && (t = this.p().host + t) : t = this.h();
                        var e = {}
                          , o = Object.entries(this.t.routes).find(function(n) {
                            return e = new P(n[0],n[1],r.t).matchesUrl(t)
                        }) || [void 0, void 0];
                        return n({
                            name: o[0]
                        }, e, {
                            route: o[1]
                        })
                    }
                    ,
                    f.h = function() {
                        var t = this.p()
                          , r = t.pathname
                          , n = t.search;
                        return (this.t.absolute ? t.host + r : r.replace(this.t.url.replace(/^\w*:\/\/[^/]+/, ""), "").replace(/^\/+/, "/")) + n
                    }
                    ,
                    f.current = function(t, r) {
                        var e = this.v()
                          , o = e.name
                          , i = e.params
                          , u = e.query
                          , f = e.route;
                        if (!t)
                            return o;
                        var a = new RegExp("^" + t.replace(/\./g, "\\.").replace(/\*/g, ".*") + "$").test(o);
                        if ([null, void 0].includes(r) || !a)
                            return a;
                        var c = new P(o,f,this.t);
                        r = this.l(r, c);
                        var l = n({}, i, u);
                        if (Object.values(r).every(function(t) {
                            return !t
                        }) && !Object.values(l).some(function(t) {
                            return void 0 !== t
                        }))
                            return !0;
                        var s = function(t, r) {
                            return Object.entries(t).every(function(t) {
                                var n = t[0]
                                  , e = t[1];
                                return Array.isArray(e) && Array.isArray(r[n]) ? e.every(function(t) {
                                    return r[n].includes(t)
                                }) : "object" == typeof e && "object" == typeof r[n] && null !== e && null !== r[n] ? s(e, r[n]) : r[n] == e
                            })
                        };
                        return s(r, l)
                    }
                    ,
                    f.p = function() {
                        var t, r, n, e, o, i, u = "undefined" != typeof window ? window.location : {}, f = u.host, a = u.pathname, c = u.search;
                        return {
                            host: null != (t = null == (r = this.t.location) ? void 0 : r.host) ? t : void 0 === f ? "" : f,
                            pathname: null != (n = null == (e = this.t.location) ? void 0 : e.pathname) ? n : void 0 === a ? "" : a,
                            search: null != (o = null == (i = this.t.location) ? void 0 : i.search) ? o : void 0 === c ? "" : c
                        }
                    }
                    ,
                    f.has = function(t) {
                        return this.t.routes.hasOwnProperty(t)
                    }
                    ,
                    f.l = function(t, r) {
                        var e = this;
                        void 0 === t && (t = {}),
                        void 0 === r && (r = this.i),
                        null != t || (t = {}),
                        t = ["string", "number"].includes(typeof t) ? [t] : t;
                        var o = r.parameterSegments.filter(function(t) {
                            return !e.t.defaults[t.name]
                        });
                        if (Array.isArray(t))
                            t = t.reduce(function(t, r, e) {
                                var i, u;
                                return n({}, t, o[e] ? ((i = {})[o[e].name] = r,
                                i) : "object" == typeof r ? r : ((u = {})[r] = "",
                                u))
                            }, {});
                        else if (1 === o.length && !t[o[0].name] && (t.hasOwnProperty(Object.values(r.bindings)[0]) || t.hasOwnProperty("id"))) {
                            var i;
                            (i = {})[o[0].name] = t,
                            t = i
                        }
                        return n({}, this.m(r), this.j(t, r))
                    }
                    ,
                    f.m = function(t) {
                        var r = this;
                        return t.parameterSegments.filter(function(t) {
                            return r.t.defaults[t.name]
                        }).reduce(function(t, e, o) {
                            var i, u = e.name;
                            return n({}, t, ((i = {})[u] = r.t.defaults[u],
                            i))
                        }, {})
                    }
                    ,
                    f.j = function(t, r) {
                        var e = r.bindings
                          , o = r.parameterSegments;
                        return Object.entries(t).reduce(function(t, r) {
                            var i, u, f = r[0], a = r[1];
                            if (!a || "object" != typeof a || Array.isArray(a) || !o.some(function(t) {
                                return t.name === f
                            }))
                                return n({}, t, ((u = {})[f] = a,
                                u));
                            if (!a.hasOwnProperty(e[f])) {
                                if (!a.hasOwnProperty("id"))
                                    throw new Error("Ziggy error: object passed as '" + f + "' parameter is missing route model binding key '" + e[f] + "'.");
                                e[f] = "id"
                            }
                            return n({}, t, ((i = {})[f] = a[e[f]],
                            i))
                        }, {})
                    }
                    ,
                    f.valueOf = function() {
                        return this.toString()
                    }
                    ,
                    r(e, [{
                        key: "params",
                        get: function() {
                            var t = this.v();
                            return n({}, t.params, t.query)
                        }
                    }, {
                        key: "routeParams",
                        get: function() {
                            return this.v().params
                        }
                    }, {
                        key: "queryParams",
                        get: function() {
                            return this.v().query
                        }
                    }])
                }(/*#__PURE__*/
                f(String));
                return function(t, r, n, e) {
                    var o = new F(t,r,n,e);
                    return t ? o.toString() : o
                }
            });
        </script>
        <link rel="preload" as="style" href="http://mem.deep-diary.com/build/assets/app-C-5ITHOa.css"/>
        <link rel="preload" as="style" href="http://mem.deep-diary.com/build/assets/Notes-PKqGBS88.css"/>
        <link rel="preload" as="style" href="http://mem.deep-diary.com/build/assets/TextInput-Cc1oAcRE.css"/>
        <link rel="preload" as="style" href="http://mem.deep-diary.com/build/assets/Errors-DNntoaV2.css"/>
        <link rel="preload" as="style" href="http://mem.deep-diary.com/build/assets/PrettyButton-D4gZQKFc.css"/>
        <link rel="preload" as="style" href="http://mem.deep-diary.com/build/assets/style-BmOrERFa.css"/>
        <link rel="preload" as="style" href="http://mem.deep-diary.com/build/assets/PrettySpan-BSOyeuvA.css"/>
        <link rel="preload" as="style" href="http://mem.deep-diary.com/build/assets/Dropdown-C71OTspL.css"/>
        <link rel="preload" as="style" href="http://mem.deep-diary.com/build/assets/LifeEvent-BIHGLm1F.css"/>
        <link rel="preload" as="style" href="http://mem.deep-diary.com/build/assets/TextArea-CcPsosLQ.css"/>
        <link rel="preload" as="style" href="http://mem.deep-diary.com/build/assets/ContactSelector-B1HxR7by.css"/>
        <link rel="preload" as="style" href="http://mem.deep-diary.com/build/assets/PrettyLink-Dux0fgYJ.css"/>
        <link rel="preload" as="style" href="http://mem.deep-diary.com/build/assets/HoverMenu-C0JtihMY.css"/>
        <link rel="preload" as="style" href="http://mem.deep-diary.com/build/assets/Show-BYWwufOE.css"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/app-oqvuHSjt.js"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/Show-DVKkVioU.js"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/DialogModal-B4JGZEu7.js"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/ConfirmationModal-Bhs2ZhOB.js"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/Button-DpzbufUl.js"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/DangerButton-DWzoKnqZ.js"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/SecondaryButton-Da9vP6fI.js"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/Layout-C6vT0vvK.js"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/_plugin-vue_export-helper-DlAUqK2U.js"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/pencil-BhIp10ZA.js"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/index-CnW85Z8r.js"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/Avatar-B3cQdmJw.js"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/Notes-ZRPSmbFA.js"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/TextInput-DX9V6GHe.js"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/Errors-BO1ws8m0.js"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/PrettyButton-BrcLq_EV.js"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/style-BBohIiXX.js"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/PrettySpan-BB5wxRlp.js"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/Dropdown-Dn1_4Z_y.js"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/createLucideIcon-BYHK-FC4.js"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/LifeEvent-CuLIvBzg.js"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/TextArea-DetahtAt.js"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/ContactSelector-D1qTpP2s.js"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/ContactCard-CQBVka5M.js"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/PrettyLink-AqoAny7R.js"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/HoverMenu-Cit37Oe4.js"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/layout-list-DLhQzYSM.js"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/Uploadcare-BC1THB2e.js"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/chevron-right-BqGi3fvX.js"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/Modal-BrSRzD2h.js"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/Pagination-C54HrCWK.js"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/calendar-days-DIU1mjMK.js"/>
        <link rel="modulepreload" href="http://mem.deep-diary.com/build/assets/omit-CUL6U2Gi.js"/>
        <link rel="stylesheet" href="http://mem.deep-diary.com/build/assets/app-C-5ITHOa.css"/>
        <link rel="stylesheet" href="http://mem.deep-diary.com/build/assets/Notes-PKqGBS88.css"/>
        <link rel="stylesheet" href="http://mem.deep-diary.com/build/assets/TextInput-Cc1oAcRE.css"/>
        <link rel="stylesheet" href="http://mem.deep-diary.com/build/assets/Errors-DNntoaV2.css"/>
        <link rel="stylesheet" href="http://mem.deep-diary.com/build/assets/PrettyButton-D4gZQKFc.css"/>
        <link rel="stylesheet" href="http://mem.deep-diary.com/build/assets/style-BmOrERFa.css"/>
        <link rel="stylesheet" href="http://mem.deep-diary.com/build/assets/PrettySpan-BSOyeuvA.css"/>
        <link rel="stylesheet" href="http://mem.deep-diary.com/build/assets/Dropdown-C71OTspL.css"/>
        <link rel="stylesheet" href="http://mem.deep-diary.com/build/assets/LifeEvent-BIHGLm1F.css"/>
        <link rel="stylesheet" href="http://mem.deep-diary.com/build/assets/TextArea-CcPsosLQ.css"/>
        <link rel="stylesheet" href="http://mem.deep-diary.com/build/assets/ContactSelector-B1HxR7by.css"/>
        <link rel="stylesheet" href="http://mem.deep-diary.com/build/assets/PrettyLink-Dux0fgYJ.css"/>
        <link rel="stylesheet" href="http://mem.deep-diary.com/build/assets/HoverMenu-C0JtihMY.css"/>
        <link rel="stylesheet" href="http://mem.deep-diary.com/build/assets/Show-BYWwufOE.css"/>
        <script type="module" src="http://mem.deep-diary.com/build/assets/app-oqvuHSjt.js"></script>
        <script type="module" src="http://mem.deep-diary.com/build/assets/Show-DVKkVioU.js"></script>
    </head>
    <body class="font-sans antialiased bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300">
        <div id="app" data-page="{&quot;component&quot;:&quot;Vault\/Contact\/Show&quot;,&quot;props&quot;:{&quot;errors&quot;:{},&quot;jetstream&quot;:{&quot;canCreateTeams&quot;:false,&quot;canManageTwoFactorAuthentication&quot;:true,&quot;canUpdatePassword&quot;:true,&quot;canUpdateProfileInformation&quot;:true,&quot;hasEmailVerification&quot;:true,&quot;flash&quot;:[],&quot;hasAccountDeletionFeatures&quot;:false,&quot;hasApiFeatures&quot;:true,&quot;hasTeamFeatures&quot;:false,&quot;hasTermsAndPrivacyPolicyFeature&quot;:true,&quot;managesProfilePhotos&quot;:false},&quot;auth&quot;:{&quot;user&quot;:{&quot;first_name&quot;:&quot;\u7ef4\u51ac&quot;,&quot;last_name&quot;:&quot;\u845b&quot;,&quot;email&quot;:&quot;deep-diary@qq.com&quot;,&quot;timezone&quot;:&quot;Asia\/Hong_Kong&quot;,&quot;is_account_administrator&quot;:true,&quot;help_shown&quot;:true,&quot;locale&quot;:&quot;zh_CN&quot;,&quot;name&quot;:&quot;\u7ef4\u51ac \u845b&quot;,&quot;locale_ietf&quot;:&quot;zh-CN&quot;,&quot;two_factor_enabled&quot;:false}},&quot;errorBags&quot;:[],&quot;help_links&quot;:{&quot;vault_create&quot;:&quot;vaults\/introduction&quot;,&quot;last_updated_contacts&quot;:&quot;vaults\/dashboard#last-updated-contacts&quot;,&quot;settings_preferences_help&quot;:&quot;user-and-account-settings\/manage-preferences#help-display&quot;,&quot;settings_preferences_language&quot;:&quot;user-and-account-settings\/manage-preferences#language&quot;,&quot;settings_preferences_contact_names&quot;:&quot;user-and-account-settings\/manage-preferences#customize-contact-names&quot;,&quot;settings_preferences_date&quot;:&quot;user-and-account-settings\/manage-preferences#date-format&quot;,&quot;settings_preferences_numerical_format&quot;:&quot;user-and-account-settings\/manage-preferences#numerical-format&quot;,&quot;settings_preferences_timezone&quot;:&quot;user-and-account-settings\/manage-preferences#timezone&quot;,&quot;settings_preferences_maps&quot;:&quot;user-and-account-settings\/manage-preferences#timezone&quot;,&quot;settings_account_deletion&quot;:&quot;user-and-account-settings\/account-deletion&quot;},&quot;help_url&quot;:&quot;https:\/\/docs.monicahq.com\/&quot;,&quot;footer&quot;:&quot;\u7248\u672c v5.0.0-beta.5 \u2014 \u63d0\u4ea4 &lt;a rel=\&quot;noopener noreferrer\&quot; target=\&quot;_blank\&quot; class=\&quot;underline text-xs dark:text-gray-100 hover:text-gray-900 hover:dark:text-gray-200\&quot; href=\&quot;https:\/\/github.com\/monicahq\/monica\/commit\/0c9a7dd1405f71fc46ea97f87b6c4ae67a423df3\&quot;&gt;0c9a7dd&lt;\/a&gt;\u3002&lt;\/p&gt;\n&quot;,&quot;ziggy&quot;:{&quot;url&quot;:&quot;http:\/\/mem.deep-diary.com&quot;,&quot;port&quot;:null,&quot;defaults&quot;:[],&quot;routes&quot;:{&quot;webauthn.auth.options&quot;:{&quot;uri&quot;:&quot;webauthn\/auth\/options&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;webauthn.auth&quot;:{&quot;uri&quot;:&quot;webauthn\/auth&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;webauthn.store.options&quot;:{&quot;uri&quot;:&quot;webauthn\/keys\/options&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;webauthn.store&quot;:{&quot;uri&quot;:&quot;webauthn\/keys&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;webauthn.destroy&quot;:{&quot;uri&quot;:&quot;webauthn\/keys\/{id}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;id&quot;]},&quot;webauthn.update&quot;:{&quot;uri&quot;:&quot;webauthn\/keys\/{id}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;id&quot;]},&quot;scribe&quot;:{&quot;uri&quot;:&quot;docs&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;scribe.postman&quot;:{&quot;uri&quot;:&quot;docs.postman&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;scribe.openapi&quot;:{&quot;uri&quot;:&quot;docs.openapi&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;login&quot;:{&quot;uri&quot;:&quot;login&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;login.store&quot;:{&quot;uri&quot;:&quot;login&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;logout&quot;:{&quot;uri&quot;:&quot;logout&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;password.request&quot;:{&quot;uri&quot;:&quot;forgot-password&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;password.reset&quot;:{&quot;uri&quot;:&quot;reset-password\/{token}&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;token&quot;]},&quot;password.email&quot;:{&quot;uri&quot;:&quot;forgot-password&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;password.update&quot;:{&quot;uri&quot;:&quot;reset-password&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;register&quot;:{&quot;uri&quot;:&quot;register&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;register.store&quot;:{&quot;uri&quot;:&quot;register&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;verification.notice&quot;:{&quot;uri&quot;:&quot;email\/verify&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;verification.verify&quot;:{&quot;uri&quot;:&quot;email\/verify\/{id}\/{hash}&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;id&quot;,&quot;hash&quot;]},&quot;verification.send&quot;:{&quot;uri&quot;:&quot;email\/verification-notification&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;user-profile-information.update&quot;:{&quot;uri&quot;:&quot;user\/profile-information&quot;,&quot;methods&quot;:[&quot;PUT&quot;]},&quot;user-password.update&quot;:{&quot;uri&quot;:&quot;user\/password&quot;,&quot;methods&quot;:[&quot;PUT&quot;]},&quot;password.confirm&quot;:{&quot;uri&quot;:&quot;user\/confirm-password&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;password.confirmation&quot;:{&quot;uri&quot;:&quot;user\/confirmed-password-status&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;password.confirm.store&quot;:{&quot;uri&quot;:&quot;user\/confirm-password&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;two-factor.login&quot;:{&quot;uri&quot;:&quot;two-factor-challenge&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;two-factor.login.store&quot;:{&quot;uri&quot;:&quot;two-factor-challenge&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;two-factor.enable&quot;:{&quot;uri&quot;:&quot;user\/two-factor-authentication&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;two-factor.confirm&quot;:{&quot;uri&quot;:&quot;user\/confirmed-two-factor-authentication&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;two-factor.disable&quot;:{&quot;uri&quot;:&quot;user\/two-factor-authentication&quot;,&quot;methods&quot;:[&quot;DELETE&quot;]},&quot;two-factor.qr-code&quot;:{&quot;uri&quot;:&quot;user\/two-factor-qr-code&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;two-factor.secret-key&quot;:{&quot;uri&quot;:&quot;user\/two-factor-secret-key&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;two-factor.recovery-codes&quot;:{&quot;uri&quot;:&quot;user\/two-factor-recovery-codes&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;terms.show&quot;:{&quot;uri&quot;:&quot;terms-of-service&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;policy.show&quot;:{&quot;uri&quot;:&quot;privacy-policy&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;profile.show&quot;:{&quot;uri&quot;:&quot;user\/profile&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;other-browser-sessions.destroy&quot;:{&quot;uri&quot;:&quot;user\/other-browser-sessions&quot;,&quot;methods&quot;:[&quot;DELETE&quot;]},&quot;current-user-photo.destroy&quot;:{&quot;uri&quot;:&quot;user\/profile-photo&quot;,&quot;methods&quot;:[&quot;DELETE&quot;]},&quot;api-tokens.index&quot;:{&quot;uri&quot;:&quot;user\/api-tokens&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;api-tokens.store&quot;:{&quot;uri&quot;:&quot;user\/api-tokens&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;api-tokens.update&quot;:{&quot;uri&quot;:&quot;user\/api-tokens\/{token}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;token&quot;]},&quot;api-tokens.destroy&quot;:{&quot;uri&quot;:&quot;user\/api-tokens\/{token}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;token&quot;]},&quot;sanctum.csrf-cookie&quot;:{&quot;uri&quot;:&quot;sanctum\/csrf-cookie&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;sabre.dav&quot;:{&quot;uri&quot;:&quot;dav\/{path?}&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;,&quot;POST&quot;,&quot;PUT&quot;,&quot;PATCH&quot;,&quot;DELETE&quot;,&quot;OPTIONS&quot;,&quot;GET&quot;,&quot;HEAD&quot;,&quot;POST&quot;,&quot;PUT&quot;,&quot;PATCH&quot;,&quot;DELETE&quot;,&quot;PROPFIND&quot;,&quot;PROPPATCH&quot;,&quot;MKCOL&quot;,&quot;COPY&quot;,&quot;MOVE&quot;,&quot;LOCK&quot;,&quot;UNLOCK&quot;,&quot;OPTIONS&quot;,&quot;REPORT&quot;,&quot;GET&quot;,&quot;HEAD&quot;,&quot;POST&quot;,&quot;PUT&quot;,&quot;PATCH&quot;,&quot;DELETE&quot;,&quot;PROPFIND&quot;,&quot;PROPPATCH&quot;,&quot;MKCOL&quot;,&quot;COPY&quot;,&quot;MOVE&quot;,&quot;LOCK&quot;,&quot;UNLOCK&quot;,&quot;OPTIONS&quot;,&quot;REPORT&quot;],&quot;wheres&quot;:{&quot;path&quot;:&quot;(.)*&quot;},&quot;parameters&quot;:[&quot;path&quot;]},&quot;api.&quot;:{&quot;uri&quot;:&quot;api\/user&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;api.users.index&quot;:{&quot;uri&quot;:&quot;api\/users&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;api.users.show&quot;:{&quot;uri&quot;:&quot;api\/users\/{user}&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;user&quot;]},&quot;api.vaults.index&quot;:{&quot;uri&quot;:&quot;api\/vaults&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;api.vaults.store&quot;:{&quot;uri&quot;:&quot;api\/vaults&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;api.vaults.show&quot;:{&quot;uri&quot;:&quot;api\/vaults\/{vault}&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;api.vaults.update&quot;:{&quot;uri&quot;:&quot;api\/vaults\/{vault}&quot;,&quot;methods&quot;:[&quot;PUT&quot;,&quot;PATCH&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;api.vaults.destroy&quot;:{&quot;uri&quot;:&quot;api\/vaults\/{vault}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;home&quot;:{&quot;uri&quot;:&quot;\/&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;login.provider&quot;:{&quot;uri&quot;:&quot;auth\/{driver}&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;driver&quot;]},&quot;invitation.show&quot;:{&quot;uri&quot;:&quot;invitation\/{code}&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;code&quot;]},&quot;invitation.store&quot;:{&quot;uri&quot;:&quot;invitation&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;vault.index&quot;:{&quot;uri&quot;:&quot;vaults&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;vault.create&quot;:{&quot;uri&quot;:&quot;vaults\/create&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;vault.store&quot;:{&quot;uri&quot;:&quot;vaults&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;vault.show&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;],&quot;bindings&quot;:{&quot;vault&quot;:&quot;id&quot;}},&quot;vault.edit&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/edit&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;],&quot;bindings&quot;:{&quot;vault&quot;:&quot;id&quot;}},&quot;vault.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;],&quot;bindings&quot;:{&quot;vault&quot;:&quot;id&quot;}},&quot;vault.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;],&quot;bindings&quot;:{&quot;vault&quot;:&quot;id&quot;}},&quot;vault.default_tab.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/defaultTab&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;vault.calendar.index&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/calendar&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;],&quot;bindings&quot;:{&quot;vault&quot;:&quot;id&quot;}},&quot;vault.calendar.month&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/calendar\/years\/{year}\/months\/{month}&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;year&quot;,&quot;month&quot;],&quot;bindings&quot;:{&quot;vault&quot;:&quot;id&quot;}},&quot;vault.calendar.day&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/calendar\/years\/{year}\/months\/{month}\/days\/{day}&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;year&quot;,&quot;month&quot;,&quot;day&quot;],&quot;bindings&quot;:{&quot;vault&quot;:&quot;id&quot;}},&quot;vault.reminder.index&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/reminders&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;vault.feed.show&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/feed&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;vault.tasks.index&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/tasks&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;vault.reports.index&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/reports&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;vault.reports.addresses.index&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/reports\/addresses&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;vault.reports.addresses.cities.show&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/reports\/addresses\/city\/{city}&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;city&quot;]},&quot;vault.reports.addresses.countries.show&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/reports\/addresses\/country\/{country}&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;country&quot;]},&quot;vault.reports.mood_tracking_events.index&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/reports\/moodTrackingEvents&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;vault.reports.important_dates.index&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/reports\/importantDates&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;vault.life_metrics.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/lifeMetrics&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;vault.life_metrics.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/lifeMetrics\/{metric}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;metric&quot;]},&quot;vault.life_metrics.contact.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/lifeMetrics\/{metric}&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;metric&quot;]},&quot;vault.life_metrics.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/lifeMetrics\/{metric}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;metric&quot;]},&quot;contact.index&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;],&quot;bindings&quot;:{&quot;vault&quot;:&quot;id&quot;}},&quot;contact.label.index&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/labels\/{label}&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;label&quot;]},&quot;contact.sort.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/sort&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;],&quot;bindings&quot;:{&quot;vault&quot;:&quot;id&quot;}},&quot;contact.create&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/create&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;],&quot;bindings&quot;:{&quot;vault&quot;:&quot;id&quot;}},&quot;contact.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;contact.show&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.edit&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/edit&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.vcard.download&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/vcard&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;],&quot;bindings&quot;:{&quot;vault&quot;:&quot;id&quot;,&quot;contact&quot;:&quot;id&quot;}},&quot;contact.quick_fact.show&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/quickFacts\/{template}&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;template&quot;]},&quot;contact.quick_fact.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/quickFacts\/{template}&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;template&quot;]},&quot;contact.quick_fact.toggle&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/quickFacts\/toggle&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.quick_fact.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/quickFacts\/{template}\/{quickFact}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;template&quot;,&quot;quickFact&quot;]},&quot;contact.quick_fact.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/quickFacts\/{template}\/{quickFact}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;template&quot;,&quot;quickFact&quot;]},&quot;contact.archive.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/toggle&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.favorite.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/toggle-favorite&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.move.show&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/move&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.move.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/move&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.blank&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/update-template&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.template.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/template&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.page.show&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/tabs\/{slug}&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;slug&quot;]},&quot;contact.avatar.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/avatar&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.avatar.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/avatar&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.feed.show&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/feed&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.date.index&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/dates&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.date.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/dates&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.date.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/dates\/{date}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;date&quot;]},&quot;contact.date.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/dates\/{date}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;date&quot;]},&quot;contact.note.index&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/notes&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.note.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/notes&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.note.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/notes\/{note}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;note&quot;]},&quot;contact.note.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/notes\/{note}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;note&quot;]},&quot;contact.goal.show&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/goals\/{goal}&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;goal&quot;]},&quot;contact.goal.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/goals&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.goal.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/goals\/{goal}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;goal&quot;]},&quot;contact.goal.streak.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/goals\/{goal}\/streaks&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;goal&quot;]},&quot;contact.goal.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/goals\/{goal}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;goal&quot;]},&quot;contact.label.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/labels&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.label.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/labels\/{label}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;label&quot;]},&quot;contact.label.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/labels\/{label}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;label&quot;]},&quot;contact.reminder.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/reminders&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.reminder.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/reminders\/{reminder}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;reminder&quot;]},&quot;contact.reminder.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/reminders\/{reminder}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;reminder&quot;]},&quot;contact.address.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/addresses&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.address.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/addresses\/{address}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;address&quot;]},&quot;contact.address.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/addresses\/{address}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;address&quot;]},&quot;contact.address.image.show&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/addresses\/{address}\/image\/{width}x{height}&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;wheres&quot;:{&quot;width&quot;:&quot;.*&quot;,&quot;height&quot;:&quot;.*&quot;},&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;address&quot;,&quot;width&quot;,&quot;height&quot;]},&quot;contact.contact_information.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/contactInformation&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.contact_information.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/contactInformation\/{info}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;info&quot;]},&quot;contact.contact_information.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/contactInformation\/{info}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;info&quot;]},&quot;contact.loan.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/loans&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.loan.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/loans\/{loan}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;loan&quot;]},&quot;contact.loan.toggle&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/loans\/{loan}\/toggle&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;loan&quot;]},&quot;contact.loan.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/loans\/{loan}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;loan&quot;]},&quot;contact.companies.list.index&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/companies\/list&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.job_information.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/jobInformation&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.job_information.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/jobInformation&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.religion.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/religion&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.relationships.create&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/relationships\/create&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.relationships.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/relationships&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.relationships.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/relationships\/{relationship}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;relationship&quot;]},&quot;contact.pet.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/pets&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.pet.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/pets\/{pet}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;pet&quot;]},&quot;contact.pet.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/pets\/{pet}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;pet&quot;]},&quot;contact.document.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/documents&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.document.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/documents\/{document}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;document&quot;]},&quot;contact.photo.index&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/photos&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.photo.show&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/photos\/{photo}&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;photo&quot;]},&quot;contact.photo.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/photos&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.photo.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/photos\/{photo}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;photo&quot;]},&quot;contact.task.index&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/tasks\/completed&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.task.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/tasks&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.task.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/tasks\/{task}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;task&quot;]},&quot;contact.task.toggle&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/tasks\/{task}\/toggle&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;task&quot;]},&quot;contact.task.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/tasks\/{task}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;task&quot;]},&quot;contact.call.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/calls&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.call.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/calls\/{call}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;call&quot;]},&quot;contact.call.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/calls\/{call}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;call&quot;]},&quot;contact.group.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/groups&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.group.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/groups\/{group}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;group&quot;]},&quot;contact.timeline_event.index&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/timelineEvents&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.timeline_event.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/timelineEvents&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;contact.timeline_event.toggle&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/timelineEvents\/{timelineEvent}\/toggle&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;timelineEvent&quot;]},&quot;contact.life_event.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/timelineEvents\/{timelineEvent}\/lifeEvents&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;timelineEvent&quot;]},&quot;contact.timeline_event.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/timelineEvents\/{timelineEvent}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;timelineEvent&quot;]},&quot;contact.life_event.edit&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/timelineEvents\/{timelineEvent}\/lifeEvents\/{lifeEvent}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;timelineEvent&quot;,&quot;lifeEvent&quot;]},&quot;contact.life_event.toggle&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/timelineEvents\/{timelineEvent}\/lifeEvents\/{lifeEvent}\/toggle&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;timelineEvent&quot;,&quot;lifeEvent&quot;]},&quot;contact.life_event.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/timelineEvents\/{timelineEvent}\/lifeEvents\/{lifeEvent}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;,&quot;timelineEvent&quot;,&quot;lifeEvent&quot;]},&quot;contact.mood_tracking_event.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/contacts\/{contact}\/moodTrackingEvents&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;contact&quot;]},&quot;group.index&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/groups&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;group.show&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/groups\/{group}&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;group&quot;]},&quot;group.edit&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/groups\/{group}\/edit&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;group&quot;]},&quot;group.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/groups\/{group}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;group&quot;]},&quot;group.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/groups\/{group}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;group&quot;]},&quot;journal.index&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;],&quot;bindings&quot;:{&quot;vault&quot;:&quot;id&quot;}},&quot;journal.create&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/create&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;],&quot;bindings&quot;:{&quot;vault&quot;:&quot;id&quot;}},&quot;journal.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;journal.show&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/{journal}&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;journal&quot;]},&quot;journal.photo.index&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/{journal}\/photos&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;journal&quot;]},&quot;journal.year&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/{journal}\/years\/{year}&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;journal&quot;,&quot;year&quot;]},&quot;journal.edit&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/{journal}\/edit&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;journal&quot;]},&quot;journal.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/{journal}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;journal&quot;]},&quot;journal.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/{journal}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;journal&quot;]},&quot;post.create&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/{journal}\/posts\/create&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;journal&quot;]},&quot;post.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/{journal}\/posts\/template\/{template}&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;journal&quot;,&quot;template&quot;]},&quot;post.show&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/{journal}\/posts\/{post}&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;journal&quot;,&quot;post&quot;]},&quot;post.edit&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/{journal}\/posts\/{post}\/edit&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;journal&quot;,&quot;post&quot;]},&quot;post.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/{journal}\/posts\/{post}\/update&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;journal&quot;,&quot;post&quot;]},&quot;post.photos.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/{journal}\/posts\/{post}\/photos&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;journal&quot;,&quot;post&quot;]},&quot;post.photos.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/{journal}\/posts\/{post}\/photos\/{photo}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;journal&quot;,&quot;post&quot;,&quot;photo&quot;]},&quot;post.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/{journal}\/posts\/{post}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;journal&quot;,&quot;post&quot;]},&quot;post.tag.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/{journal}\/posts\/{post}\/tags&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;journal&quot;,&quot;post&quot;]},&quot;post.tag.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/{journal}\/posts\/{post}\/tags\/{tag}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;journal&quot;,&quot;post&quot;,&quot;tag&quot;]},&quot;post.tag.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/{journal}\/posts\/{post}\/tags\/{tag}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;journal&quot;,&quot;post&quot;,&quot;tag&quot;]},&quot;post.slices.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/{journal}\/posts\/{post}\/slices&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;journal&quot;,&quot;post&quot;]},&quot;post.slices.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/{journal}\/posts\/{post}\/slices&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;journal&quot;,&quot;post&quot;]},&quot;post.metrics.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/{journal}\/posts\/{post}\/metrics&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;journal&quot;,&quot;post&quot;]},&quot;post.metrics.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/{journal}\/posts\/{post}\/metrics\/{metric}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;journal&quot;,&quot;post&quot;,&quot;metric&quot;]},&quot;slices.index&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/{journal}\/slices&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;journal&quot;]},&quot;slices.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/{journal}\/slices&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;journal&quot;]},&quot;slices.show&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/{journal}\/slices\/{slice}&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;journal&quot;,&quot;slice&quot;]},&quot;slices.edit&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/{journal}\/slices\/{slice}\/edit&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;journal&quot;,&quot;slice&quot;]},&quot;slices.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/{journal}\/slices\/{slice}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;journal&quot;,&quot;slice&quot;]},&quot;slices.cover.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/{journal}\/slices\/{slice}\/cover&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;journal&quot;,&quot;slice&quot;]},&quot;slices.cover.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/{journal}\/slices\/{slice}\/cover&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;journal&quot;,&quot;slice&quot;]},&quot;slices.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/{journal}\/slices\/{slice}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;journal&quot;,&quot;slice&quot;]},&quot;journal_metrics.index&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/{journal}\/metrics&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;journal&quot;]},&quot;journal_metrics.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/{journal}\/metrics&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;journal&quot;]},&quot;journal_metrics.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/journals\/{journal}\/metrics\/{metric}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;journal&quot;,&quot;metric&quot;]},&quot;vault.files.index&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/files&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;vault.files.photos&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/files\/photos&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;vault.files.documents&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/files\/documents&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;vault.files.avatars&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/files\/avatars&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;vault.files.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/files\/{file}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;file&quot;]},&quot;vault.companies.index&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/companies&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;vault.companies.show&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/companies\/{company}&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;company&quot;]},&quot;vault.settings.index&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;vault.settings.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;vault.settings.template.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings\/template&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;vault.settings.user.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings\/users&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;vault.settings.user.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings\/users\/{user}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;user&quot;]},&quot;vault.settings.user.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings\/users\/{user}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;user&quot;]},&quot;vault.settings.label.index&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings\/labels&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;vault.settings.label.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings\/labels&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;vault.settings.label.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings\/labels\/{label}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;label&quot;]},&quot;vault.settings.label.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings\/labels\/{label}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;label&quot;]},&quot;vault.settings.tag.index&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings\/tags&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;vault.settings.tag.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings\/tags&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;vault.settings.tag.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings\/tags\/{tag}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;tag&quot;]},&quot;vault.settings.tag.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings\/tags\/{tag}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;tag&quot;]},&quot;vault.settings.important_date_type.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings\/contactImportantDateTypes&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;vault.settings.important_date_type.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings\/contactImportantDateTypes\/{type}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;type&quot;]},&quot;vault.settings.important_date_type.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings\/contactImportantDateTypes\/{type}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;type&quot;]},&quot;vault.settings.tab.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings\/visibility&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;vault.settings.mood_tracking_parameter.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings\/moodTrackingParameters&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;vault.settings.mood_tracking_parameter.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings\/moodTrackingParameters\/{parameter}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;parameter&quot;]},&quot;vault.settings.mood_tracking_parameter.order.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings\/moodTrackingParameters\/{parameter}\/order&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;parameter&quot;]},&quot;vault.settings.mood_tracking_parameter.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings\/moodTrackingParameters\/{parameter}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;parameter&quot;]},&quot;vault.settings.life_event_categories.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings\/lifeEventCategories&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;vault.settings.life_event_categories.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings\/lifeEventCategories\/{lifeEventCategory}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;lifeEventCategory&quot;]},&quot;vault.settings.life_event_categories.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings\/lifeEventCategories\/{lifeEventCategory}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;lifeEventCategory&quot;]},&quot;vault.settings.life_event_categories.order.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings\/lifeEventCategories\/{lifeEventCategory}\/order&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;lifeEventCategory&quot;]},&quot;vault.settings.life_event_types.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings\/lifeEventCategories\/{lifeEventCategory}\/lifeEventTypes&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;lifeEventCategory&quot;]},&quot;vault.settings.life_event_types.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings\/lifeEventCategories\/{lifeEventCategory}\/lifeEventTypes\/{lifeEventType}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;lifeEventCategory&quot;,&quot;lifeEventType&quot;]},&quot;vault.settings.life_event_types.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings\/lifeEventCategories\/{lifeEventCategory}\/lifeEventTypes\/{lifeEventType}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;lifeEventCategory&quot;,&quot;lifeEventType&quot;]},&quot;vault.settings.life_event_types.order.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings\/lifeEventCategories\/{lifeEventCategory}\/lifeEventTypes\/{lifeEventType}\/order&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;lifeEventCategory&quot;,&quot;lifeEventType&quot;]},&quot;vault.settings.quick_fact_templates.store&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings\/quickFactTemplates&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;vault.settings.quick_fact_templates.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings\/quickFactTemplates\/{template}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;template&quot;]},&quot;vault.settings.quick_fact_templates.order.update&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings\/quickFactTemplates\/{template}\/order&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;template&quot;]},&quot;vault.settings.quick_fact_templates.destroy&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/settings\/quickFactTemplates\/{template}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;vault&quot;,&quot;template&quot;]},&quot;vault.search.index&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/search&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;vault.search.show&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/search&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;vault.user.search.mostconsulted&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/search\/user\/contact\/mostConsulted&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;vault.user.search.index&quot;:{&quot;uri&quot;:&quot;vaults\/{vault}\/search\/user\/contacts&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;vault&quot;]},&quot;settings.index&quot;:{&quot;uri&quot;:&quot;settings&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;settings.preferences.index&quot;:{&quot;uri&quot;:&quot;settings\/preferences&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;settings.preferences.name.store&quot;:{&quot;uri&quot;:&quot;settings\/preferences\/name&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;settings.preferences.date.store&quot;:{&quot;uri&quot;:&quot;settings\/preferences\/date&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;settings.preferences.timezone.store&quot;:{&quot;uri&quot;:&quot;settings\/preferences\/timezone&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;settings.preferences.number.store&quot;:{&quot;uri&quot;:&quot;settings\/preferences\/number&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;settings.preferences.distance.store&quot;:{&quot;uri&quot;:&quot;settings\/preferences\/distance&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;settings.preferences.maps.store&quot;:{&quot;uri&quot;:&quot;settings\/preferences\/maps&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;settings.preferences.locale.store&quot;:{&quot;uri&quot;:&quot;settings\/preferences\/locale&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;settings.preferences.help.store&quot;:{&quot;uri&quot;:&quot;settings\/preferences\/help&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;settings.notifications.index&quot;:{&quot;uri&quot;:&quot;settings\/notifications&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;settings.notifications.store&quot;:{&quot;uri&quot;:&quot;settings\/notifications&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;settings.notifications.telegram.store&quot;:{&quot;uri&quot;:&quot;settings\/notifications\/telegram&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;settings.notifications.verification.store&quot;:{&quot;uri&quot;:&quot;settings\/notifications\/{notification}\/verify\/{uuid}&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;notification&quot;,&quot;uuid&quot;]},&quot;settings.notifications.test.store&quot;:{&quot;uri&quot;:&quot;settings\/notifications\/{notification}\/test&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;notification&quot;]},&quot;settings.notifications.toggle.update&quot;:{&quot;uri&quot;:&quot;settings\/notifications\/{notification}\/toggle&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;notification&quot;]},&quot;settings.notifications.destroy&quot;:{&quot;uri&quot;:&quot;settings\/notifications\/{notification}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;notification&quot;]},&quot;settings.notifications.log.index&quot;:{&quot;uri&quot;:&quot;settings\/notifications\/{notification}\/logs&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;notification&quot;]},&quot;settings.user.index&quot;:{&quot;uri&quot;:&quot;settings\/users&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;settings.user.create&quot;:{&quot;uri&quot;:&quot;settings\/users\/create&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;settings.user.store&quot;:{&quot;uri&quot;:&quot;settings\/users&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;settings.user.show&quot;:{&quot;uri&quot;:&quot;settings\/users\/{user}&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;user&quot;]},&quot;settings.user.update&quot;:{&quot;uri&quot;:&quot;settings\/users\/{user}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;user&quot;]},&quot;settings.user.destroy&quot;:{&quot;uri&quot;:&quot;settings\/users\/{user}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;user&quot;]},&quot;settings.personalize.index&quot;:{&quot;uri&quot;:&quot;settings\/personalize&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;settings.personalize.relationship.index&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/relationships&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;settings.personalize.relationship.grouptype.store&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/relationships&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;settings.personalize.relationship.grouptype.update&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/relationships\/{groupType}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;groupType&quot;]},&quot;settings.personalize.relationship.grouptype.destroy&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/relationships\/{groupType}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;groupType&quot;]},&quot;settings.personalize.relationship.type.store&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/relationships\/{groupType}\/types&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;groupType&quot;]},&quot;settings.personalize.relationship.type.update&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/relationships\/{groupType}\/types\/{type}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;groupType&quot;,&quot;type&quot;]},&quot;settings.personalize.relationship.type.destroy&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/relationships\/{groupType}\/types\/{type}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;groupType&quot;,&quot;type&quot;]},&quot;settings.personalize.call_reasons.index&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/callReasonTypes&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;settings.personalize.call_reasons.type.store&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/callReasonTypes&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;settings.personalize.call_reasons.type.update&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/callReasonTypes\/{callReasonType}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;callReasonType&quot;]},&quot;settings.personalize.call_reasons.type.destroy&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/callReasonTypes\/{callReasonType}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;callReasonType&quot;]},&quot;settings.personalize.call_reasons.store&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/callReasonTypes\/{callReasonType}\/reasons&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;callReasonType&quot;]},&quot;settings.personalize.call_reasons.update&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/callReasonTypes\/{callReasonType}\/reasons\/{reason}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;callReasonType&quot;,&quot;reason&quot;]},&quot;settings.personalize.call_reasons.destroy&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/callReasonTypes\/{callReasonType}\/reasons\/{reason}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;callReasonType&quot;,&quot;reason&quot;]},&quot;settings.personalize.gift_occasions.index&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/giftOccasions&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;settings.personalize.gift_occasions.store&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/giftOccasions&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;settings.personalize.gift_occasions.update&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/giftOccasions\/{giftOccasion}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;giftOccasion&quot;]},&quot;settings.personalize.gift_occasions.destroy&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/giftOccasions\/{giftOccasion}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;giftOccasion&quot;]},&quot;settings.personalize.gift_occasions.order.update&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/giftOccasions\/{giftOccasion}\/position&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;giftOccasion&quot;]},&quot;settings.personalize.gift_states.index&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/giftStates&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;settings.personalize.gift_states.store&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/giftStates&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;settings.personalize.gift_states.update&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/giftStates\/{giftState}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;giftState&quot;]},&quot;settings.personalize.gift_states.destroy&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/giftStates\/{giftState}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;giftState&quot;]},&quot;settings.personalize.gift_states.order.update&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/giftStates\/{giftState}\/position&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;giftState&quot;]},&quot;settings.personalize.post_templates.index&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/postTemplates&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;settings.personalize.post_templates.store&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/postTemplates&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;settings.personalize.post_templates.update&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/postTemplates\/{postTemplate}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;postTemplate&quot;]},&quot;settings.personalize.post_templates.destroy&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/postTemplates\/{postTemplate}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;postTemplate&quot;]},&quot;settings.personalize.post_templates.order.update&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/postTemplates\/{postTemplate}\/position&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;postTemplate&quot;]},&quot;settings.personalize.post_templates.section.store&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/postTemplates\/{postTemplate}\/sections&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;postTemplate&quot;]},&quot;settings.personalize.post_templates.section.update&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/postTemplates\/{postTemplate}\/sections\/{section}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;postTemplate&quot;,&quot;section&quot;]},&quot;settings.personalize.post_templates.section.destroy&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/postTemplates\/{postTemplate}\/sections\/{section}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;postTemplate&quot;,&quot;section&quot;]},&quot;settings.personalize.post_templates.section.order.update&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/postTemplates\/{postTemplate}\/sections\/{section}\/position&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;postTemplate&quot;,&quot;section&quot;]},&quot;settings.personalize.group_types.index&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/groupTypes&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;settings.personalize.group_types.store&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/groupTypes&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;settings.personalize.group_types.update&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/groupTypes\/{type}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;type&quot;]},&quot;settings.personalize.group_types.destroy&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/groupTypes\/{type}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;type&quot;]},&quot;settings.personalize.group_types.order.update&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/groupTypes\/{type}\/position&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;type&quot;]},&quot;settings.personalize.group_types.roles.store&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/groupTypes\/{type}\/groupTypeRoles&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;type&quot;]},&quot;settings.personalize.group_types.roles.update&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/groupTypes\/{type}\/groupTypeRoles\/{role}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;type&quot;,&quot;role&quot;]},&quot;settings.personalize.group_types.roles.destroy&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/groupTypes\/{type}\/groupTypeRoles\/{role}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;type&quot;,&quot;role&quot;]},&quot;settings.personalize.group_types.roles.order.update&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/groupTypes\/{type}\/groupTypeRoles\/{role}\/position&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;type&quot;,&quot;role&quot;]},&quot;settings.personalize.gender.index&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/genders&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;settings.personalize.gender.store&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/genders&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;settings.personalize.gender.update&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/genders\/{gender}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;gender&quot;]},&quot;settings.personalize.gender.destroy&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/genders\/{gender}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;gender&quot;]},&quot;settings.personalize.pronoun.index&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/pronouns&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;settings.personalize.pronoun.store&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/pronouns&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;settings.personalize.pronoun.update&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/pronouns\/{pronoun}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;pronoun&quot;]},&quot;settings.personalize.pronoun.destroy&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/pronouns\/{pronoun}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;pronoun&quot;]},&quot;settings.personalize.address_type.index&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/addressTypes&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;settings.personalize.address_type.store&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/addressTypes&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;settings.personalize.address_type.update&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/addressTypes\/{addressType}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;addressType&quot;]},&quot;settings.personalize.address_type.destroy&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/addressTypes\/{addressType}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;addressType&quot;]},&quot;settings.personalize.pet_category.index&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/petCategories&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;settings.personalize.pet_category.store&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/petCategories&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;settings.personalize.pet_category.update&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/petCategories\/{petCategory}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;petCategory&quot;]},&quot;settings.personalize.pet_category.destroy&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/petCategories\/{petCategory}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;petCategory&quot;]},&quot;settings.personalize.contact_information_type.index&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/contactInformationType&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;settings.personalize.contact_information_type.store&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/contactInformationType&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;settings.personalize.contact_information_type.update&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/contactInformationType\/{type}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;type&quot;]},&quot;settings.personalize.contact_information_type.destroy&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/contactInformationType\/{type}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;type&quot;]},&quot;settings.personalize.template.index&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/templates&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;settings.personalize.template.store&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/templates&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;settings.personalize.template.update&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/templates\/{template}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;template&quot;]},&quot;settings.personalize.template.destroy&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/templates\/{template}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;template&quot;]},&quot;settings.personalize.template.show&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/templates\/{template}&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;template&quot;]},&quot;settings.personalize.template.template_page.store&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/templates\/{template}&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;template&quot;]},&quot;settings.personalize.template.template_page.update&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/templates\/{template}\/template_pages\/{page}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;template&quot;,&quot;page&quot;]},&quot;settings.personalize.template.template_page.destroy&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/templates\/{template}\/template_pages\/{page}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;template&quot;,&quot;page&quot;]},&quot;settings.personalize.template.template_page.show&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/templates\/{template}\/template_pages\/{page}&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;],&quot;parameters&quot;:[&quot;template&quot;,&quot;page&quot;]},&quot;settings.personalize.template.template_page.order.update&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/templates\/{template}\/template_pages\/{page}\/order&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;template&quot;,&quot;page&quot;]},&quot;settings.personalize.template.template_page.module.store&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/templates\/{template}\/template_pages\/{page}\/modules&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;template&quot;,&quot;page&quot;]},&quot;settings.personalize.template.template_page.module.order.update&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/templates\/{template}\/template_pages\/{page}\/modules\/{module}\/order&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;template&quot;,&quot;page&quot;,&quot;module&quot;]},&quot;settings.personalize.template.template_page.module.destroy&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/templates\/{template}\/template_pages\/{page}\/modules\/{module}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;template&quot;,&quot;page&quot;,&quot;module&quot;]},&quot;settings.personalize.module.index&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/modules&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;settings.personalize.module.store&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/modules&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;settings.personalize.module.update&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/modules\/{module}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;module&quot;]},&quot;settings.personalize.module.destroy&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/modules\/{module}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;module&quot;]},&quot;settings.personalize.currency.index&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/currencies&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;settings.personalize.currency.update&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/currencies\/{currency}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;currency&quot;]},&quot;settings.personalize.currency.store&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/currencies&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;settings.personalize.currency.destroy&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/currencies&quot;,&quot;methods&quot;:[&quot;DELETE&quot;]},&quot;settings.personalize.religions.index&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/religions&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;settings.personalize.religions.store&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/religions&quot;,&quot;methods&quot;:[&quot;POST&quot;]},&quot;settings.personalize.religions.update&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/religions\/{religion}&quot;,&quot;methods&quot;:[&quot;PUT&quot;],&quot;parameters&quot;:[&quot;religion&quot;]},&quot;settings.personalize.religions.destroy&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/religions\/{religion}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;religion&quot;]},&quot;settings.personalize.religions.order.update&quot;:{&quot;uri&quot;:&quot;settings\/personalize\/religions\/{religion}\/position&quot;,&quot;methods&quot;:[&quot;POST&quot;],&quot;parameters&quot;:[&quot;religion&quot;]},&quot;settings.storage.index&quot;:{&quot;uri&quot;:&quot;settings\/storage&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;settings.cancel.index&quot;:{&quot;uri&quot;:&quot;settings\/cancel&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;settings.cancel.destroy&quot;:{&quot;uri&quot;:&quot;settings\/cancel&quot;,&quot;methods&quot;:[&quot;PUT&quot;]},&quot;currencies.index&quot;:{&quot;uri&quot;:&quot;currencies&quot;,&quot;methods&quot;:[&quot;GET&quot;,&quot;HEAD&quot;]},&quot;provider.delete&quot;:{&quot;uri&quot;:&quot;auth\/{driver}&quot;,&quot;methods&quot;:[&quot;DELETE&quot;],&quot;parameters&quot;:[&quot;driver&quot;]}},&quot;location&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/tabs\/information&quot;},&quot;sentry&quot;:{&quot;dsn&quot;:null,&quot;tunnel&quot;:&quot;\/sentry\/tunnel&quot;,&quot;release&quot;:&quot;v5.0.0-beta.5&quot;,&quot;environment&quot;:null,&quot;sendDefaultPii&quot;:false,&quot;tracesSampleRate&quot;:0},&quot;layoutData&quot;:{&quot;user&quot;:{&quot;id&quot;:&quot;019b6547-fa8f-7227-a0a3-790e82058356&quot;,&quot;name&quot;:&quot;\u7ef4\u51ac \u845b&quot;},&quot;vault&quot;:{&quot;id&quot;:&quot;019ba163-d71f-70d0-b3cc-f8a53413f24b&quot;,&quot;name&quot;:&quot;test&quot;,&quot;permission&quot;:{&quot;at_least_editor&quot;:true,&quot;at_least_manager&quot;:true},&quot;visibility&quot;:{&quot;show_group_tab&quot;:true,&quot;show_tasks_tab&quot;:true,&quot;show_files_tab&quot;:true,&quot;show_journal_tab&quot;:true,&quot;show_companies_tab&quot;:true,&quot;show_reports_tab&quot;:true,&quot;show_calendar_tab&quot;:true},&quot;url&quot;:{&quot;dashboard&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b&quot;,&quot;contacts&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts&quot;,&quot;calendar&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/calendar&quot;,&quot;journals&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/journals&quot;,&quot;groups&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/groups&quot;,&quot;companies&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/companies&quot;,&quot;tasks&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/tasks&quot;,&quot;files&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/files&quot;,&quot;reports&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/reports&quot;,&quot;settings&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/settings&quot;,&quot;search&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/search&quot;,&quot;get_most_consulted_contacts&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/search\/user\/contact\/mostConsulted&quot;,&quot;search_contacts_only&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/search\/user\/contacts&quot;}},&quot;url&quot;:{&quot;vaults&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults&quot;,&quot;settings&quot;:&quot;http:\/\/mem.deep-diary.com\/settings&quot;,&quot;logout&quot;:&quot;http:\/\/mem.deep-diary.com\/logout&quot;}},&quot;data&quot;:{&quot;contact_name&quot;:{&quot;name&quot;:&quot;\u7ef4\u51ac \u845b&quot;,&quot;is_favorite&quot;:0,&quot;url&quot;:{&quot;edit&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/edit&quot;,&quot;toggle_favorite&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/toggle-favorite&quot;}},&quot;listed&quot;:true,&quot;template_pages&quot;:{&quot;1&quot;:{&quot;id&quot;:2,&quot;name&quot;:&quot;\u6d3b\u52a8\u63d0\u8981&quot;,&quot;selected&quot;:false,&quot;url&quot;:{&quot;show&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/tabs\/activity-feed&quot;}},&quot;2&quot;:{&quot;id&quot;:3,&quot;name&quot;:&quot;\u8fde\u63a5\u65b9\u5f0f&quot;,&quot;selected&quot;:false,&quot;url&quot;:{&quot;show&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/tabs\/ways-to-connect&quot;}},&quot;3&quot;:{&quot;id&quot;:4,&quot;name&quot;:&quot;\u793e\u4f1a\u7684&quot;,&quot;selected&quot;:false,&quot;url&quot;:{&quot;show&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/tabs\/social&quot;}},&quot;4&quot;:{&quot;id&quot;:5,&quot;name&quot;:&quot;\u751f\u6d3b\u76ee\u6807&quot;,&quot;selected&quot;:false,&quot;url&quot;:{&quot;show&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/tabs\/life-goals&quot;}},&quot;5&quot;:{&quot;id&quot;:6,&quot;name&quot;:&quot;\u4fe1\u606f&quot;,&quot;selected&quot;:true,&quot;url&quot;:{&quot;show&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/tabs\/information&quot;}}},&quot;contact_information&quot;:[{&quot;id&quot;:1,&quot;type&quot;:&quot;avatar&quot;,&quot;data&quot;:{&quot;avatar&quot;:{&quot;type&quot;:&quot;svg&quot;,&quot;content&quot;:&quot;&lt;svg xmlns=\&quot;http:\/\/www.w3.org\/2000\/svg\&quot; viewBox=\&quot;0 0 231 231\&quot;&gt;&lt;path d=\&quot;M33.83,33.83a115.5,115.5,0,1,1,0,163.34,115.49,115.49,0,0,1,0-163.34Z\&quot; style=\&quot;fill:#00a58c;\&quot;\/&gt;&lt;path d=\&quot;m115.5 51.75a63.75 63.75 0 0 0-10.5 126.63v14.09a115.5 115.5 0 0 0-53.729 19.027 115.5 115.5 0 0 0 128.46 0 115.5 115.5 0 0 0-53.729-19.029v-14.084a63.75 63.75 0 0 0 53.25-62.881 63.75 63.75 0 0 0-63.65-63.75 63.75 63.75 0 0 0-0.09961 0z\&quot; style=\&quot;fill:#755227;\&quot;\/&gt;&lt;path d=\&quot;m141.75 195a114.79 114.79 0 0 1 38 16.5 115.53 115.53 0 0 1-128.46 0 114.79 114.79 0 0 1 38-16.5c0 10.76 11.75 19.48 26.25 19.48s26.25-8.72 26.25-19.48z\&quot; style=\&quot;fill:#fff;\&quot;\/&gt;&lt;path d=\&quot;m92.502 194.27v0.70391c0 4.3033 2.4373 8.2583 6.3807 11.183 4.2199 3.1204 10.106 5.0508 16.661 5.0508 6.548 0 12.434-1.9303 16.654-5.0508 3.9434-2.9245 6.388-6.8795 6.388-11.183v-0.67489c1.0768 0.21771 2.1463 0.44994 3.2158 0.69666h-7e-3c1.0695 0.24672 2.1318 0.50798 3.1867 0.791-0.27648 6.103-3.6524 11.553-8.9708 15.493-5.2821 3.9114-12.521 6.328-20.466 6.328-7.9449 0-15.184-2.4165-20.474-6.328-5.333-3.9477-8.7089-9.4194-8.9708-15.544 1.055-0.27577 2.1099-0.53702 3.1722-0.78376 1.0695-0.23947 2.1463-0.46443 3.2304-0.68213z\&quot; style=\&quot;fill:#000;\&quot;\/&gt;&lt;path d=\&quot;m41.835 75.131c-2.8674 12.582 1.2304 27.241 6.0238 39.031 0.25861 0.63658 0.51208 1.3075 0.79989 1.9683 0.71726 1.658 2.1184 3.9751 3.0038 3.9266 0.56895-0.0312 0.71637-1.5512 1.0228-3.1562 2.1988-19.097 8.8981-27.915 15.636-38.107 2.8783-4.0645 3.8616-7.2293 1.0644-9.9325-6.3236-3.5596-14.924-2.8574-21.367-0.67406-3.2312 1.4765-5.2427 3.4773-6.1842 6.9439zm125.65-8.5679c7.65-0.70616 19.714-0.1307 21.694 8.5679 1.455 6.4083 0.26915 17.747-1.0542 24.579-1.1961 5.3203-3.8066 14.231-7.8782 19.75-0.5565 0.44544-0.96888 0.13656-1.4159-1.1606-0.90692-3.0353-1.4298-7.8372-2.2556-10.727-3.4822-12.79-8.2195-21.875-14.429-29.94-5.5782-6.8415-4.2152-9.7207 5.3393-11.069z\&quot; style=\&quot;fill:#efefef;\&quot;\/&gt;&lt;path d=\&quot;m112.27 73.826c-18.585-7.5217-34.987-14.797-48.939 5.018-4.9752 7.083-3.7876 8.8056-4.9217 0.0749-1.637-12.476-4.7505-34.174 1.9259-45.194 7.6822-12.7 19.323-13.128 31.039-5.3818 10.796 7.7784 24.277 14.647 38.015 12.219 12.732-2.2576 15.835-7.7464 15.707-19.912-0.0215-2.6-0.0963-5.2106-0.2033-7.7999 13.631 3.9267 24.609 14.776 26.513 29.049 0.88804 6.6336 0.26749 12.722-1.9259 19.013-5.9702 17.108-30.119 20.896-45.74 16.841-3.9588-1.0378-7.6822-2.4181-11.47-3.9267z\&quot; style=\&quot;fill:none;\&quot;\/&gt;&lt;path d=\&quot;m86.851 100.39a4.94 4.94 0 1 0 4.9297 5 5 5 0 0 0-4.9297-5zm57.221 0a4.94 4.94 0 1 0 4.9394 4.9394 4.94 4.94 0 0 0-4.9394-4.9394z\&quot; style=\&quot;fill:#000;\&quot;\/&gt;&lt;path d=\&quot;m86.207 89.365c-25.504 0-21.503 6.8561-21.035 19.596 0.80177 18.121 17.763 16.514 21.201 16.639 14.758-0.041 20.518-8.227 22.951-22.932 1.8166-10.731-9.251-13.174-23.117-13.303zm58.598 0c-13.866 0.1284-24.936 2.5717-23.119 13.303 2.4332 14.705 8.1936 22.891 22.951 22.932 3.4383-0.125 20.399 1.4828 21.201-16.639 0-18.965-0.47958-19.596-21.033-19.596z\&quot; style=\&quot;fill:#000;\&quot;\/&gt;&lt;path d=\&quot;m169.87 90.255a0.51 0.51 0 0 0-0.43991-0.52 167.64 167.64 0 0 0-22.6-1.6801c-12 0-27.47 3.7601-30.17 3.7601h-2.4c-1.2499 0-5.29-0.80996-10.45-1.6801a124.35 124.35 0 0 0-19.72-2.08 166.18 166.18 0 0 0-19.31 1.24c-1.56 0.17999-2.69 0.35009-3.2899 0.44009a0.51 0.51 0 0 0-0.44007 0.52l-0.091 6.4501a0.57 0.57 0 0 0 0.33012 0.52l0.73994 0.23992c1.08 0.41992 1.0001 19.85 6.78 24.71 3.4401 2.8599 6.51 4.4899 19.42 4.4899 7.4699 0 12.17-1.9999 16.63-8 3.21-4.32 6.0999-14.55 6.0999-14.55 0.82006-4.07 3.7702-4.52 4.43-4.5801h0.12068c0.11078 0 3.66 0.0593 4.57 4.5801 0 0 2.8599 10.22 6.0699 14.54 4.4601 5.9999 9.1601 8 16.63 8 12.91 0 16-1.63 19.42-4.4901 5.7898-4.86 5.6998-24.29 6.78-24.71l0.73994-0.23993a0.57 0.57 0 0 0 0.32996-0.52l-0.12068-6.4501zm-65 23c-1.9101 4.5-6.8 10.29-13.7 10.64-20.7 0.99985-21.65-4.7401-23-9.3201a31.45 31.45 0 0 1-1.2099-13.18c0.53997-4.5799 1.7-7.2699 3.7801-8.6201a9.3 9.3 0 0 1 4.3499-1.51 85.07 85.07 0 0 1 11.4-0.52 59.23 59.23 0 0 1 9.2099 0.69999c7.37 1.2 12.35 3.7001 12.35 6.1601a46.12 46.12 0 0 1-3.23 15.64zm58 1.3201c-1.34 4.5799-2.29 10.36-23 9.3201-6.91-0.3501-11.81-6.1401-13.71-10.64a46.35 46.35 0 0 1-3.22-15.64c0-3.39 9.43-6.8599 21.56-6.8599 12.13 0 14 0.89996 15.75 1.9999 2.08 1.3502 3.2398 4 3.77 8.6201a31.23 31.23 0 0 1-1.1601 13.17z\&quot; style=\&quot;fill:#57FFFD;\&quot;\/&gt;&lt;path d=\&quot;m100.19 152.09c2.8726 4.0616 9.8095 4.7232 15.119-0.45432 5.0656 4.5134 11.167 5.6898 15.495 0.31458\&quot; style=\&quot;fill:none;stroke-linecap:round;stroke-linejoin:round;stroke-width:5.8949;stroke:#222;\&quot;\/&gt;&lt;path d=\&quot;m109.67 135.53c-0.9758 0.0743-2.05 0.45327-3.1485 0.99414-4.3235 2.1399-7.3862 4.2557-10.639 7.1406-0.6251 0.5715 0.1168 0.77785 1.4238 0.87304 5.6967 0.0536 14.384 0.41404 15.098-0.875 1.9251-2.0788 1.7969-5.3303-0.1816-7.3008-0.701-0.67533-1.5769-0.90632-2.5527-0.83203zm11.656 0c-0.9758-0.0743-1.8517 0.1567-2.5527 0.83203-1.9785 1.9705-2.1067 5.222-0.1817 7.3008 0.7142 1.289 9.401 0.9286 15.098 0.875 1.307-0.0952 2.0489-0.30154 1.4238-0.87304-3.2524-2.8849-6.3151-5.0007-10.639-7.1406-1.0985-0.54087-2.1727-0.91985-3.1485-0.99414z\&quot; style=\&quot;fill:#fff;\&quot;\/&gt;&lt;\/svg&gt;&quot;}}},{&quot;id&quot;:2,&quot;type&quot;:&quot;contact_names&quot;,&quot;data&quot;:{&quot;name&quot;:&quot;\u7ef4\u51ac \u845b&quot;,&quot;is_favorite&quot;:0,&quot;url&quot;:{&quot;edit&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/edit&quot;,&quot;toggle_favorite&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/toggle-favorite&quot;}}},{&quot;id&quot;:3,&quot;type&quot;:&quot;family_summary&quot;,&quot;data&quot;:{&quot;family_relationships&quot;:[],&quot;love_relationships&quot;:[]}},{&quot;id&quot;:4,&quot;type&quot;:&quot;important_dates&quot;,&quot;data&quot;:{&quot;dates&quot;:[{&quot;id&quot;:8,&quot;label&quot;:&quot;\u751f\u65e5&quot;,&quot;date&quot;:&quot;1\u6708 02, 2026&quot;,&quot;type&quot;:&quot;\u51fa\u751f\u65e5\u671f&quot;,&quot;age&quot;:0}],&quot;url&quot;:{&quot;edit&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/dates&quot;}}},{&quot;id&quot;:5,&quot;type&quot;:&quot;gender_pronoun&quot;,&quot;data&quot;:{&quot;gender&quot;:null,&quot;pronoun&quot;:null,&quot;url&quot;:{&quot;edit&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/edit&quot;}}},{&quot;id&quot;:6,&quot;type&quot;:&quot;labels&quot;,&quot;data&quot;:{&quot;labels_in_contact&quot;:[],&quot;labels_in_vault&quot;:[],&quot;url&quot;:{&quot;store&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/labels&quot;,&quot;update&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/dates&quot;}}},{&quot;id&quot;:7,&quot;type&quot;:&quot;company&quot;,&quot;data&quot;:{&quot;job_position&quot;:null,&quot;company&quot;:null,&quot;url&quot;:{&quot;index&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/companies\/list&quot;,&quot;update&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/jobInformation&quot;,&quot;destroy&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/jobInformation&quot;}}},{&quot;id&quot;:8,&quot;type&quot;:&quot;religions&quot;,&quot;data&quot;:{&quot;religion&quot;:null,&quot;religions&quot;:[{&quot;id&quot;:1,&quot;name&quot;:&quot;\u57fa\u7763\u6559&quot;,&quot;selected&quot;:false},{&quot;id&quot;:2,&quot;name&quot;:&quot;\u7a46\u65af\u6797&quot;,&quot;selected&quot;:false},{&quot;id&quot;:3,&quot;name&quot;:&quot;\u5370\u5ea6\u6559&quot;,&quot;selected&quot;:false},{&quot;id&quot;:4,&quot;name&quot;:&quot;\u4f5b\u6559\u5f92&quot;,&quot;selected&quot;:false},{&quot;id&quot;:5,&quot;name&quot;:&quot;\u795e\u9053\u6559&quot;,&quot;selected&quot;:false},{&quot;id&quot;:6,&quot;name&quot;:&quot;\u9053\u6559&quot;,&quot;selected&quot;:false},{&quot;id&quot;:7,&quot;name&quot;:&quot;\u9521\u514b\u6559&quot;,&quot;selected&quot;:false},{&quot;id&quot;:8,&quot;name&quot;:&quot;\u72b9&quot;,&quot;selected&quot;:false},{&quot;id&quot;:9,&quot;name&quot;:&quot;\u65e0\u795e\u8bba\u8005&quot;,&quot;selected&quot;:false}],&quot;url&quot;:{&quot;update&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/religion&quot;}}}],&quot;group_summary_information&quot;:[],&quot;quick_fact_template_entries&quot;:{&quot;show_quick_facts&quot;:true,&quot;templates&quot;:[{&quot;id&quot;:13,&quot;label&quot;:&quot;\u5174\u8da3\u7231\u597d&quot;,&quot;url&quot;:{&quot;show&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/quickFacts\/13&quot;}},{&quot;id&quot;:14,&quot;label&quot;:&quot;\u98df\u7269\u504f\u597d&quot;,&quot;url&quot;:{&quot;show&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/quickFacts\/14&quot;}}],&quot;quick_facts&quot;:{&quot;template&quot;:{&quot;id&quot;:13,&quot;label&quot;:&quot;\u5174\u8da3\u7231\u597d&quot;,&quot;url&quot;:{&quot;store&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/quickFacts\/13&quot;}},&quot;quick_facts&quot;:[{&quot;id&quot;:29,&quot;content&quot;:&quot;\u5174\u8da3\u7231\u597d\u6d4b\u8bd5&quot;,&quot;url&quot;:{&quot;update&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/quickFacts\/13\/29&quot;,&quot;destroy&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/quickFacts\/13\/29&quot;}}]},&quot;url&quot;:{&quot;toggle&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/quickFacts\/toggle&quot;}},&quot;modules&quot;:[{&quot;id&quot;:17,&quot;type&quot;:&quot;documents&quot;,&quot;data&quot;:{&quot;documents&quot;:[],&quot;uploadcare&quot;:{&quot;publicKey&quot;:&quot;9e3d287cf39505fd319c&quot;,&quot;signature&quot;:&quot;d16afc6a121002f8ace2aacd03f72caeecb0cf8563033df4c54b737ab9fc8c59&quot;,&quot;expire&quot;:1767957936},&quot;canUploadFile&quot;:true,&quot;url&quot;:{&quot;store&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/documents&quot;}}},{&quot;id&quot;:18,&quot;type&quot;:&quot;photos&quot;,&quot;data&quot;:{&quot;photos&quot;:[],&quot;uploadcare&quot;:{&quot;publicKey&quot;:&quot;9e3d287cf39505fd319c&quot;,&quot;signature&quot;:&quot;d16afc6a121002f8ace2aacd03f72caeecb0cf8563033df4c54b737ab9fc8c59&quot;,&quot;expire&quot;:1767957936},&quot;canUploadFile&quot;:true,&quot;url&quot;:{&quot;index&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/photos&quot;,&quot;store&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/photos&quot;}}},{&quot;id&quot;:19,&quot;type&quot;:&quot;notes&quot;,&quot;data&quot;:{&quot;notes&quot;:[{&quot;id&quot;:2,&quot;body&quot;:&quot;\u8868\u793a\u4e0d\u5012\u7fc1\u673a\u68b0\u7ed3\u6784\u9700\u8981\u6539\u5584\n\u66f4\u65b0\u4e86\u4e0b&quot;,&quot;body_excerpt&quot;:null,&quot;show_full_content&quot;:false,&quot;title&quot;:&quot;\u8ba8\u8bba\u4e0d\u5012\u7fc1\u7ed3\u6784&quot;,&quot;emotion&quot;:{&quot;id&quot;:2,&quot;name&quot;:&quot;\ud83d\ude36\u200d\ud83c\udf2b\ufe0f\u4e2d\u6027&quot;},&quot;author&quot;:{&quot;id&quot;:&quot;019ba163-d7a3-72b5-96b5-ba4ea81c0406&quot;,&quot;name&quot;:&quot;\u7ef4\u51ac \u845b&quot;,&quot;avatar&quot;:{&quot;type&quot;:&quot;svg&quot;,&quot;content&quot;:&quot;&lt;svg xmlns=\&quot;http:\/\/www.w3.org\/2000\/svg\&quot; viewBox=\&quot;0 0 231 231\&quot;&gt;&lt;path d=\&quot;M33.83,33.83a115.5,115.5,0,1,1,0,163.34,115.49,115.49,0,0,1,0-163.34Z\&quot; style=\&quot;fill:#00a58c;\&quot;\/&gt;&lt;path d=\&quot;m115.5 51.75a63.75 63.75 0 0 0-10.5 126.63v14.09a115.5 115.5 0 0 0-53.729 19.027 115.5 115.5 0 0 0 128.46 0 115.5 115.5 0 0 0-53.729-19.029v-14.084a63.75 63.75 0 0 0 53.25-62.881 63.75 63.75 0 0 0-63.65-63.75 63.75 63.75 0 0 0-0.09961 0z\&quot; style=\&quot;fill:#755227;\&quot;\/&gt;&lt;path d=\&quot;m141.75 195a114.79 114.79 0 0 1 38 16.5 115.53 115.53 0 0 1-128.46 0 114.79 114.79 0 0 1 38-16.5c0 10.76 11.75 19.48 26.25 19.48s26.25-8.72 26.25-19.48z\&quot; style=\&quot;fill:#fff;\&quot;\/&gt;&lt;path d=\&quot;m92.502 194.27v0.70391c0 4.3033 2.4373 8.2583 6.3807 11.183 4.2199 3.1204 10.106 5.0508 16.661 5.0508 6.548 0 12.434-1.9303 16.654-5.0508 3.9434-2.9245 6.388-6.8795 6.388-11.183v-0.67489c1.0768 0.21771 2.1463 0.44994 3.2158 0.69666h-7e-3c1.0695 0.24672 2.1318 0.50798 3.1867 0.791-0.27648 6.103-3.6524 11.553-8.9708 15.493-5.2821 3.9114-12.521 6.328-20.466 6.328-7.9449 0-15.184-2.4165-20.474-6.328-5.333-3.9477-8.7089-9.4194-8.9708-15.544 1.055-0.27577 2.1099-0.53702 3.1722-0.78376 1.0695-0.23947 2.1463-0.46443 3.2304-0.68213z\&quot; style=\&quot;fill:#000;\&quot;\/&gt;&lt;path d=\&quot;m41.835 75.131c-2.8674 12.582 1.2304 27.241 6.0238 39.031 0.25861 0.63658 0.51208 1.3075 0.79989 1.9683 0.71726 1.658 2.1184 3.9751 3.0038 3.9266 0.56895-0.0312 0.71637-1.5512 1.0228-3.1562 2.1988-19.097 8.8981-27.915 15.636-38.107 2.8783-4.0645 3.8616-7.2293 1.0644-9.9325-6.3236-3.5596-14.924-2.8574-21.367-0.67406-3.2312 1.4765-5.2427 3.4773-6.1842 6.9439zm125.65-8.5679c7.65-0.70616 19.714-0.1307 21.694 8.5679 1.455 6.4083 0.26915 17.747-1.0542 24.579-1.1961 5.3203-3.8066 14.231-7.8782 19.75-0.5565 0.44544-0.96888 0.13656-1.4159-1.1606-0.90692-3.0353-1.4298-7.8372-2.2556-10.727-3.4822-12.79-8.2195-21.875-14.429-29.94-5.5782-6.8415-4.2152-9.7207 5.3393-11.069z\&quot; style=\&quot;fill:#efefef;\&quot;\/&gt;&lt;path d=\&quot;m112.27 73.826c-18.585-7.5217-34.987-14.797-48.939 5.018-4.9752 7.083-3.7876 8.8056-4.9217 0.0749-1.637-12.476-4.7505-34.174 1.9259-45.194 7.6822-12.7 19.323-13.128 31.039-5.3818 10.796 7.7784 24.277 14.647 38.015 12.219 12.732-2.2576 15.835-7.7464 15.707-19.912-0.0215-2.6-0.0963-5.2106-0.2033-7.7999 13.631 3.9267 24.609 14.776 26.513 29.049 0.88804 6.6336 0.26749 12.722-1.9259 19.013-5.9702 17.108-30.119 20.896-45.74 16.841-3.9588-1.0378-7.6822-2.4181-11.47-3.9267z\&quot; style=\&quot;fill:none;\&quot;\/&gt;&lt;path d=\&quot;m86.851 100.39a4.94 4.94 0 1 0 4.9297 5 5 5 0 0 0-4.9297-5zm57.221 0a4.94 4.94 0 1 0 4.9394 4.9394 4.94 4.94 0 0 0-4.9394-4.9394z\&quot; style=\&quot;fill:#000;\&quot;\/&gt;&lt;path d=\&quot;m86.207 89.365c-25.504 0-21.503 6.8561-21.035 19.596 0.80177 18.121 17.763 16.514 21.201 16.639 14.758-0.041 20.518-8.227 22.951-22.932 1.8166-10.731-9.251-13.174-23.117-13.303zm58.598 0c-13.866 0.1284-24.936 2.5717-23.119 13.303 2.4332 14.705 8.1936 22.891 22.951 22.932 3.4383-0.125 20.399 1.4828 21.201-16.639 0-18.965-0.47958-19.596-21.033-19.596z\&quot; style=\&quot;fill:#000;\&quot;\/&gt;&lt;path d=\&quot;m169.87 90.255a0.51 0.51 0 0 0-0.43991-0.52 167.64 167.64 0 0 0-22.6-1.6801c-12 0-27.47 3.7601-30.17 3.7601h-2.4c-1.2499 0-5.29-0.80996-10.45-1.6801a124.35 124.35 0 0 0-19.72-2.08 166.18 166.18 0 0 0-19.31 1.24c-1.56 0.17999-2.69 0.35009-3.2899 0.44009a0.51 0.51 0 0 0-0.44007 0.52l-0.091 6.4501a0.57 0.57 0 0 0 0.33012 0.52l0.73994 0.23992c1.08 0.41992 1.0001 19.85 6.78 24.71 3.4401 2.8599 6.51 4.4899 19.42 4.4899 7.4699 0 12.17-1.9999 16.63-8 3.21-4.32 6.0999-14.55 6.0999-14.55 0.82006-4.07 3.7702-4.52 4.43-4.5801h0.12068c0.11078 0 3.66 0.0593 4.57 4.5801 0 0 2.8599 10.22 6.0699 14.54 4.4601 5.9999 9.1601 8 16.63 8 12.91 0 16-1.63 19.42-4.4901 5.7898-4.86 5.6998-24.29 6.78-24.71l0.73994-0.23993a0.57 0.57 0 0 0 0.32996-0.52l-0.12068-6.4501zm-65 23c-1.9101 4.5-6.8 10.29-13.7 10.64-20.7 0.99985-21.65-4.7401-23-9.3201a31.45 31.45 0 0 1-1.2099-13.18c0.53997-4.5799 1.7-7.2699 3.7801-8.6201a9.3 9.3 0 0 1 4.3499-1.51 85.07 85.07 0 0 1 11.4-0.52 59.23 59.23 0 0 1 9.2099 0.69999c7.37 1.2 12.35 3.7001 12.35 6.1601a46.12 46.12 0 0 1-3.23 15.64zm58 1.3201c-1.34 4.5799-2.29 10.36-23 9.3201-6.91-0.3501-11.81-6.1401-13.71-10.64a46.35 46.35 0 0 1-3.22-15.64c0-3.39 9.43-6.8599 21.56-6.8599 12.13 0 14 0.89996 15.75 1.9999 2.08 1.3502 3.2398 4 3.77 8.6201a31.23 31.23 0 0 1-1.1601 13.17z\&quot; style=\&quot;fill:#57FFFD;\&quot;\/&gt;&lt;path d=\&quot;m100.19 152.09c2.8726 4.0616 9.8095 4.7232 15.119-0.45432 5.0656 4.5134 11.167 5.6898 15.495 0.31458\&quot; style=\&quot;fill:none;stroke-linecap:round;stroke-linejoin:round;stroke-width:5.8949;stroke:#222;\&quot;\/&gt;&lt;path d=\&quot;m109.67 135.53c-0.9758 0.0743-2.05 0.45327-3.1485 0.99414-4.3235 2.1399-7.3862 4.2557-10.639 7.1406-0.6251 0.5715 0.1168 0.77785 1.4238 0.87304 5.6967 0.0536 14.384 0.41404 15.098-0.875 1.9251-2.0788 1.7969-5.3303-0.1816-7.3008-0.701-0.67533-1.5769-0.90632-2.5527-0.83203zm11.656 0c-0.9758-0.0743-1.8517 0.1567-2.5527 0.83203-1.9785 1.9705-2.1067 5.222-0.1817 7.3008 0.7142 1.289 9.401 0.9286 15.098 0.875 1.307-0.0952 2.0489-0.30154 1.4238-0.87304-3.2524-2.8849-6.3151-5.0007-10.639-7.1406-1.0985-0.54087-2.1727-0.91985-3.1485-0.99414z\&quot; style=\&quot;fill:#fff;\&quot;\/&gt;&lt;\/svg&gt;&quot;},&quot;url&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406&quot;},&quot;written_at&quot;:&quot;1\u6708 09, 2026&quot;,&quot;url&quot;:{&quot;update&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/notes\/2&quot;,&quot;destroy&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/notes\/2&quot;}}],&quot;emotions&quot;:[{&quot;id&quot;:1,&quot;name&quot;:&quot;\ud83d\ude21 \u8d1f\u9762&quot;,&quot;type&quot;:&quot;negative&quot;},{&quot;id&quot;:2,&quot;name&quot;:&quot;\ud83d\ude36\u200d\ud83c\udf2b\ufe0f\u4e2d\u6027&quot;,&quot;type&quot;:&quot;neutral&quot;},{&quot;id&quot;:3,&quot;name&quot;:&quot;\ud83d\ude01 \u79ef\u6781&quot;,&quot;type&quot;:&quot;positive&quot;}],&quot;url&quot;:{&quot;store&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/notes&quot;,&quot;index&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/notes&quot;}}},{&quot;id&quot;:20,&quot;type&quot;:&quot;reminders&quot;,&quot;data&quot;:{&quot;reminders&quot;:[{&quot;id&quot;:12,&quot;label&quot;:&quot;\u751f\u65e5&quot;,&quot;date&quot;:&quot;1\u6708 02, 2026&quot;,&quot;type&quot;:&quot;recurring_year&quot;,&quot;frequency_number&quot;:1,&quot;day&quot;:2,&quot;month&quot;:1,&quot;choice&quot;:&quot;full_date&quot;,&quot;reminder_choice&quot;:&quot;recurring&quot;,&quot;url&quot;:{&quot;update&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/reminders\/12&quot;,&quot;destroy&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/reminders\/12&quot;}},{&quot;id&quot;:8,&quot;label&quot;:&quot;test remender update&quot;,&quot;date&quot;:&quot;1\u6708 10, 2026&quot;,&quot;type&quot;:&quot;recurring_year&quot;,&quot;frequency_number&quot;:1,&quot;day&quot;:10,&quot;month&quot;:1,&quot;choice&quot;:&quot;full_date&quot;,&quot;reminder_choice&quot;:&quot;recurring&quot;,&quot;url&quot;:{&quot;update&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/reminders\/8&quot;,&quot;destroy&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/reminders\/8&quot;}}],&quot;months&quot;:[{&quot;id&quot;:1,&quot;name&quot;:&quot;\u4e00\u6708&quot;},{&quot;id&quot;:2,&quot;name&quot;:&quot;\u4e8c\u6708&quot;},{&quot;id&quot;:3,&quot;name&quot;:&quot;\u4e09\u6708&quot;},{&quot;id&quot;:4,&quot;name&quot;:&quot;\u56db\u6708&quot;},{&quot;id&quot;:5,&quot;name&quot;:&quot;\u4e94\u6708&quot;},{&quot;id&quot;:6,&quot;name&quot;:&quot;\u516d\u6708&quot;},{&quot;id&quot;:7,&quot;name&quot;:&quot;\u4e03\u6708&quot;},{&quot;id&quot;:8,&quot;name&quot;:&quot;\u516b\u6708&quot;},{&quot;id&quot;:9,&quot;name&quot;:&quot;\u4e5d\u6708&quot;},{&quot;id&quot;:10,&quot;name&quot;:&quot;\u5341\u6708&quot;},{&quot;id&quot;:11,&quot;name&quot;:&quot;\u5341\u4e00\u6708&quot;},{&quot;id&quot;:12,&quot;name&quot;:&quot;\u5341\u4e8c\u6708&quot;}],&quot;days&quot;:[{&quot;id&quot;:1,&quot;name&quot;:1},{&quot;id&quot;:2,&quot;name&quot;:2},{&quot;id&quot;:3,&quot;name&quot;:3},{&quot;id&quot;:4,&quot;name&quot;:4},{&quot;id&quot;:5,&quot;name&quot;:5},{&quot;id&quot;:6,&quot;name&quot;:6},{&quot;id&quot;:7,&quot;name&quot;:7},{&quot;id&quot;:8,&quot;name&quot;:8},{&quot;id&quot;:9,&quot;name&quot;:9},{&quot;id&quot;:10,&quot;name&quot;:10},{&quot;id&quot;:11,&quot;name&quot;:11},{&quot;id&quot;:12,&quot;name&quot;:12},{&quot;id&quot;:13,&quot;name&quot;:13},{&quot;id&quot;:14,&quot;name&quot;:14},{&quot;id&quot;:15,&quot;name&quot;:15},{&quot;id&quot;:16,&quot;name&quot;:16},{&quot;id&quot;:17,&quot;name&quot;:17},{&quot;id&quot;:18,&quot;name&quot;:18},{&quot;id&quot;:19,&quot;name&quot;:19},{&quot;id&quot;:20,&quot;name&quot;:20},{&quot;id&quot;:21,&quot;name&quot;:21},{&quot;id&quot;:22,&quot;name&quot;:22},{&quot;id&quot;:23,&quot;name&quot;:23},{&quot;id&quot;:24,&quot;name&quot;:24},{&quot;id&quot;:25,&quot;name&quot;:25},{&quot;id&quot;:26,&quot;name&quot;:26},{&quot;id&quot;:27,&quot;name&quot;:27},{&quot;id&quot;:28,&quot;name&quot;:28},{&quot;id&quot;:29,&quot;name&quot;:29},{&quot;id&quot;:30,&quot;name&quot;:30},{&quot;id&quot;:31,&quot;name&quot;:31}],&quot;url&quot;:{&quot;store&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/reminders&quot;}}},{&quot;id&quot;:21,&quot;type&quot;:&quot;loans&quot;,&quot;data&quot;:{&quot;loans&quot;:[],&quot;current_date&quot;:&quot;2026-01-09&quot;,&quot;url&quot;:{&quot;currencies&quot;:&quot;http:\/\/mem.deep-diary.com\/currencies&quot;,&quot;store&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/loans&quot;}}},{&quot;id&quot;:22,&quot;type&quot;:&quot;tasks&quot;,&quot;data&quot;:{&quot;tasks&quot;:[{&quot;id&quot;:14,&quot;label&quot;:&quot;\u6d4b\u8bd5\u4eba\u7269&quot;,&quot;description&quot;:null,&quot;completed&quot;:false,&quot;completed_at&quot;:null,&quot;due_at&quot;:{&quot;formatted&quot;:&quot;1\u6708 10, 2026&quot;,&quot;value&quot;:&quot;2026-01-10&quot;,&quot;is_late&quot;:false},&quot;url&quot;:{&quot;update&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/tasks\/14&quot;,&quot;toggle&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/tasks\/14\/toggle&quot;,&quot;destroy&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/tasks\/14&quot;}}],&quot;completed_tasks_count&quot;:0,&quot;url&quot;:{&quot;completed&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/tasks\/completed&quot;,&quot;store&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/tasks&quot;}}},{&quot;id&quot;:23,&quot;type&quot;:&quot;calls&quot;,&quot;data&quot;:{&quot;contact_name&quot;:&quot;\u7ef4\u51ac \u845b&quot;,&quot;calls&quot;:[{&quot;id&quot;:14,&quot;called_at&quot;:&quot;1\u6708 01, 2026&quot;,&quot;duration&quot;:null,&quot;description&quot;:&quot;\u6d4b\u8bd5 \u97f3\u9891\u901a\u8bdd&quot;,&quot;who_initiated&quot;:&quot;me&quot;,&quot;type&quot;:&quot;audio&quot;,&quot;answered&quot;:true,&quot;emotion&quot;:{&quot;id&quot;:3,&quot;name&quot;:&quot;\ud83d\ude01 \u79ef\u6781&quot;,&quot;type&quot;:&quot;positive&quot;},&quot;reason&quot;:{&quot;id&quot;:5,&quot;label&quot;:&quot;\u6765\u542c\u542c\u4ed6\u4eec\u7684\u6545\u4e8b&quot;},&quot;url&quot;:{&quot;update&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/calls\/14&quot;,&quot;destroy&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/calls\/14&quot;}},{&quot;id&quot;:15,&quot;called_at&quot;:&quot;12\u6708 26, 2025&quot;,&quot;duration&quot;:null,&quot;description&quot;:&quot;\u6d4b\u8bd5 \u89c6\u9891\u901a\u8bdd&quot;,&quot;who_initiated&quot;:&quot;me&quot;,&quot;type&quot;:&quot;video&quot;,&quot;answered&quot;:true,&quot;emotion&quot;:{&quot;id&quot;:3,&quot;name&quot;:&quot;\ud83d\ude01 \u79ef\u6781&quot;,&quot;type&quot;:&quot;positive&quot;},&quot;reason&quot;:{&quot;id&quot;:5,&quot;label&quot;:&quot;\u6765\u542c\u542c\u4ed6\u4eec\u7684\u6545\u4e8b&quot;},&quot;url&quot;:{&quot;update&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/calls\/15&quot;,&quot;destroy&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/calls\/15&quot;}}],&quot;emotions&quot;:[{&quot;id&quot;:1,&quot;name&quot;:&quot;\ud83d\ude21 \u8d1f\u9762&quot;,&quot;type&quot;:&quot;negative&quot;},{&quot;id&quot;:2,&quot;name&quot;:&quot;\ud83d\ude36\u200d\ud83c\udf2b\ufe0f\u4e2d\u6027&quot;,&quot;type&quot;:&quot;neutral&quot;},{&quot;id&quot;:3,&quot;name&quot;:&quot;\ud83d\ude01 \u79ef\u6781&quot;,&quot;type&quot;:&quot;positive&quot;}],&quot;call_reason_types&quot;:[{&quot;id&quot;:1,&quot;label&quot;:&quot;\u4e2a\u4eba\u7684&quot;,&quot;reasons&quot;:[{&quot;id&quot;:1,&quot;label&quot;:&quot;\u54a8\u8be2&quot;},{&quot;id&quot;:2,&quot;label&quot;:&quot;\u53ea\u662f\u6253\u4e2a\u62db\u547c&quot;},{&quot;id&quot;:3,&quot;label&quot;:&quot;\u770b\u770b\u4ed6\u4eec\u662f\u5426\u9700\u8981\u4ec0\u4e48&quot;},{&quot;id&quot;:4,&quot;label&quot;:&quot;\u51fa\u4e8e\u5c0a\u91cd\u548c\u6b23\u8d4f&quot;},{&quot;id&quot;:5,&quot;label&quot;:&quot;\u6765\u542c\u542c\u4ed6\u4eec\u7684\u6545\u4e8b&quot;}]},{&quot;id&quot;:2,&quot;label&quot;:&quot;\u5546\u4e1a&quot;,&quot;reasons&quot;:[{&quot;id&quot;:6,&quot;label&quot;:&quot;\u8ba8\u8bba\u6700\u8fd1\u8d2d\u4e70\u7684\u5546\u54c1&quot;},{&quot;id&quot;:7,&quot;label&quot;:&quot;\u8ba8\u8bba\u5408\u4f5c\u4f19\u4f34\u5173\u7cfb&quot;}]}],&quot;url&quot;:{&quot;store&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/calls&quot;}}},{&quot;id&quot;:24,&quot;type&quot;:&quot;posts&quot;,&quot;data&quot;:[]},{&quot;id&quot;:10,&quot;type&quot;:&quot;addresses&quot;,&quot;data&quot;:{&quot;active_addresses&quot;:[{&quot;id&quot;:15,&quot;is_past_address&quot;:false,&quot;line_1&quot;:&quot;\u6d4b\u8bd5\u5730\u5740 \u5de5\u4f5c&quot;,&quot;line_2&quot;:null,&quot;city&quot;:&quot;\u6d4b\u8bd5\u57ce\u5e02&quot;,&quot;province&quot;:&quot;\u6d4b\u8bd5\u7701\u4efd&quot;,&quot;postal_code&quot;:null,&quot;country&quot;:&quot;\u4e2d\u56fd&quot;,&quot;type&quot;:{&quot;id&quot;:3,&quot;name&quot;:&quot;\ud83c\udfe2 \u5de5\u4f5c&quot;},&quot;url&quot;:{&quot;show&quot;:&quot;https:\/\/www.openstreetmap.org\/search?query=%E6%B5%8B%E8%AF%95%E5%9C%B0%E5%9D%80+%E5%B7%A5%E4%BD%9C+%E6%B5%8B%E8%AF%95%E5%9F%8E%E5%B8%82+%E6%B5%8B%E8%AF%95%E7%9C%81%E4%BB%BD+%E4%B8%AD%E5%9B%BD&quot;,&quot;update&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/addresses\/15&quot;,&quot;destroy&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/addresses\/15&quot;}},{&quot;id&quot;:16,&quot;is_past_address&quot;:false,&quot;line_1&quot;:&quot;\u6d4b\u8bd5\u5730\u5740 \u5c0f\u6728\u5c4b&quot;,&quot;line_2&quot;:null,&quot;city&quot;:&quot;\u6d4b\u8bd5\u57ce\u5e02&quot;,&quot;province&quot;:&quot;\u6d4b\u8bd5\u7701\u4efd&quot;,&quot;postal_code&quot;:null,&quot;country&quot;:&quot;\u4e2d\u56fd&quot;,&quot;type&quot;:{&quot;id&quot;:4,&quot;name&quot;:&quot;\ud83c\udf33 \u5c0f\u6728\u5c4b&quot;},&quot;url&quot;:{&quot;show&quot;:&quot;https:\/\/www.openstreetmap.org\/search?query=%E6%B5%8B%E8%AF%95%E5%9C%B0%E5%9D%80+%E5%B0%8F%E6%9C%A8%E5%B1%8B+%E6%B5%8B%E8%AF%95%E5%9F%8E%E5%B8%82+%E6%B5%8B%E8%AF%95%E7%9C%81%E4%BB%BD+%E4%B8%AD%E5%9B%BD&quot;,&quot;update&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/addresses\/16&quot;,&quot;destroy&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/addresses\/16&quot;}},{&quot;id&quot;:17,&quot;is_past_address&quot;:false,&quot;line_1&quot;:&quot;\u6d4b\u8bd5\u5730\u5740 \u5176\u4ed6&quot;,&quot;line_2&quot;:null,&quot;city&quot;:&quot;\u6d4b\u8bd5\u57ce\u5e02&quot;,&quot;province&quot;:&quot;\u6d4b\u8bd5\u7701\u4efd&quot;,&quot;postal_code&quot;:null,&quot;country&quot;:&quot;\u4e2d\u56fd&quot;,&quot;type&quot;:{&quot;id&quot;:5,&quot;name&quot;:&quot;\u2754\u5176\u4ed6&quot;},&quot;url&quot;:{&quot;show&quot;:&quot;https:\/\/www.openstreetmap.org\/search?query=%E6%B5%8B%E8%AF%95%E5%9C%B0%E5%9D%80+%E5%85%B6%E4%BB%96+%E6%B5%8B%E8%AF%95%E5%9F%8E%E5%B8%82+%E6%B5%8B%E8%AF%95%E7%9C%81%E4%BB%BD+%E4%B8%AD%E5%9B%BD&quot;,&quot;update&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/addresses\/17&quot;,&quot;destroy&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/addresses\/17&quot;}}],&quot;inactive_addresses&quot;:[],&quot;address_types&quot;:[{&quot;id&quot;:1,&quot;name&quot;:&quot;\ud83c\udfe1 \u4e3b\u9875&quot;,&quot;selected&quot;:false},{&quot;id&quot;:2,&quot;name&quot;:&quot;\ud83c\udfe0 \u7b2c\u4e8c\u5c45\u6240&quot;,&quot;selected&quot;:false},{&quot;id&quot;:3,&quot;name&quot;:&quot;\ud83c\udfe2 \u5de5\u4f5c&quot;,&quot;selected&quot;:false},{&quot;id&quot;:4,&quot;name&quot;:&quot;\ud83c\udf33 \u5c0f\u6728\u5c4b&quot;,&quot;selected&quot;:false},{&quot;id&quot;:5,&quot;name&quot;:&quot;\u2754\u5176\u4ed6&quot;,&quot;selected&quot;:false}],&quot;addresses_in_vault&quot;:[{&quot;id&quot;:15,&quot;address&quot;:&quot;\u6d4b\u8bd5\u5730\u5740 \u5de5\u4f5c \u6d4b\u8bd5\u57ce\u5e02 \u6d4b\u8bd5\u7701\u4efd \u4e2d\u56fd&quot;},{&quot;id&quot;:16,&quot;address&quot;:&quot;\u6d4b\u8bd5\u5730\u5740 \u5c0f\u6728\u5c4b \u6d4b\u8bd5\u57ce\u5e02 \u6d4b\u8bd5\u7701\u4efd \u4e2d\u56fd&quot;},{&quot;id&quot;:17,&quot;address&quot;:&quot;\u6d4b\u8bd5\u5730\u5740 \u5176\u4ed6 \u6d4b\u8bd5\u57ce\u5e02 \u6d4b\u8bd5\u7701\u4efd \u4e2d\u56fd&quot;}],&quot;url&quot;:{&quot;store&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/addresses&quot;}}},{&quot;id&quot;:11,&quot;type&quot;:&quot;contact_information&quot;,&quot;data&quot;:{&quot;contact_information&quot;:[{&quot;id&quot;:56,&quot;label&quot;:&quot;deep-diary@qq.com&quot;,&quot;protocol&quot;:&quot;mailto:&quot;,&quot;data&quot;:&quot;deep-diary@qq.com&quot;,&quot;data_with_protocol&quot;:&quot;mailto:deep-diary@qq.com&quot;,&quot;contact_information_type&quot;:{&quot;id&quot;:1,&quot;name&quot;:&quot;\u7535\u5b50\u90ae\u4ef6\u5730\u5740&quot;},&quot;url&quot;:{&quot;update&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/contactInformation\/56&quot;,&quot;destroy&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/contactInformation\/56&quot;}},{&quot;id&quot;:58,&quot;label&quot;:&quot;test@example.com&quot;,&quot;protocol&quot;:&quot;mailto:&quot;,&quot;data&quot;:&quot;test@example.com&quot;,&quot;data_with_protocol&quot;:&quot;mailto:test@example.com&quot;,&quot;contact_information_type&quot;:{&quot;id&quot;:1,&quot;name&quot;:&quot;\u7535\u5b50\u90ae\u4ef6\u5730\u5740&quot;},&quot;url&quot;:{&quot;update&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/contactInformation\/58&quot;,&quot;destroy&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/contactInformation\/58&quot;}}],&quot;contact_information_types&quot;:[{&quot;id&quot;:1,&quot;name&quot;:&quot;\u7535\u5b50\u90ae\u4ef6\u5730\u5740&quot;},{&quot;id&quot;:2,&quot;name&quot;:&quot;\u7535\u8bdd&quot;},{&quot;id&quot;:3,&quot;name&quot;:&quot;Facebook&quot;},{&quot;id&quot;:4,&quot;name&quot;:&quot;Twitter&quot;},{&quot;id&quot;:5,&quot;name&quot;:&quot;Whatsapp&quot;},{&quot;id&quot;:6,&quot;name&quot;:&quot;Telegram&quot;},{&quot;id&quot;:7,&quot;name&quot;:&quot;Hangouts&quot;},{&quot;id&quot;:8,&quot;name&quot;:&quot;Linkedin&quot;},{&quot;id&quot;:9,&quot;name&quot;:&quot;Instagram&quot;}],&quot;url&quot;:{&quot;store&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/contactInformation&quot;}}}],&quot;avatar&quot;:{&quot;uploadcare&quot;:{&quot;publicKey&quot;:&quot;9e3d287cf39505fd319c&quot;,&quot;signature&quot;:&quot;d16afc6a121002f8ace2aacd03f72caeecb0cf8563033df4c54b737ab9fc8c59&quot;,&quot;expire&quot;:1767957936},&quot;canUploadFile&quot;:true,&quot;hasFile&quot;:false},&quot;options&quot;:{&quot;can_be_archived&quot;:false,&quot;can_be_deleted&quot;:false},&quot;url&quot;:{&quot;toggle_archive&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/toggle&quot;,&quot;update_avatar&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/avatar&quot;,&quot;destroy_avatar&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/avatar&quot;,&quot;update_template&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/update-template&quot;,&quot;move_contact&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/move&quot;,&quot;destroy&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406&quot;,&quot;download_vcard&quot;:&quot;http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/vcard&quot;}}},&quot;url&quot;:&quot;\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/tabs\/information&quot;,&quot;version&quot;:&quot;acee3fd1bd5f605440b5b5ff8a889b53&quot;,&quot;clearHistory&quot;:false,&quot;encryptHistory&quot;:false}"></div>
    </body>
</html>
