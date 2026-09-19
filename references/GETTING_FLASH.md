# Obtaining FLASH for ScientificBrain Physics Skills

FLASH source code is **not bundledled or mirrored** in this repository. Obtain it directly from the Flash Center for Computational Science.

## Official process

1. Open the official Code Request page:
   https://flash.rochester.edu/site/flashcode/coderequest.html

2. Complete the registration/code-request form. The Flash Center asks for identity/affiliation information, intended research use, and acceptance of the FLASH license agreement.

3. If the request is approved, the Flash Center provides credentials for the download service.

4. Download FLASH from the official download page:
   https://flash.rochester.edu/site/flashcode/download/

5. Keep the original archive and license information according to the terms supplied by the Flash Center. Do not commit the FLASH source tree or archive into this repository.

## Local installation contract

Extract FLASH locally, for example:

```text
/opt/scientificbrain/solvers/FLASH4.8/
```

Then expose it to the skills through an environment variable:

```bash
export FLASH_ROOT=/opt/scientificbrain/solvers/FLASH4.8
python scripts/flash_inventory.py --flash-root "$FLASH_ROOT"
```

The toolkit expects a real FLASH source tree containing `RELEASE`, `source/`, setup tooling, and the appropriate site/compiler configuration.

## Core build dependencies

The current FLASH user guide lists a Fortran compiler, C compiler, MPI, and the required I/O/scientific libraries as part of the platform requirements. Exact compiler/library combinations vary by platform and FLASH configuration, so inspect the release notes and site configuration for the installation being used.

## Do not automate credential scraping

The FLASH registration/download path is a licensed access flow. ScientificBrain should not attempt to bypass registration, CAPTCHA, license acceptance, or credential controls. A user or administrator obtains FLASH legitimately and mounts the resulting local installation for the solver skills.

## Publication acknowledgment

The FLASH license/code-request page requires an acknowledgment in publications resulting from FLASH usage. Use the **exact current wording on the official page** at publication time rather than copying a possibly stale version into ScientificBrain.

## Verification

After installation:

```bash
export FLASH_ROOT=/path/to/FLASH4.8
python scripts/flash_inventory.py --flash-root "$FLASH_ROOT"
```

Then begin with a small official benchmark before configuring a research campaign.
