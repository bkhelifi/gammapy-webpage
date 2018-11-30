#!/usr/bin/env python
"""Make the gammapy.org static webpage.

This is very much work in progress.
Probably we should add a static website build step.
"""
import logging
import json
import os
from pathlib import Path
import click

log = logging.getLogger(__name__)


class Dataset:
    """Dataset base class.

    The Dataset class has a local_repo property where to scan the content
    and a base_url to build access links for each file.

    A dataset has a name as identifier.
    It also has a description and list of files, each file has a given URL
    and a path that tells you where the file will be placed when downloaded.
    TODO: Add MD5 checksums and file sizes.

    If you want to add a dataset, make a new class and add it to the list below.
    """

    base_url = "https://github.com/gammapy/gammapy-extra/raw/master/datasets"
    local_repo = Path(os.environ["GAMMAPY_EXTRA"]) / "datasets"

    @property
    def record(self):
        return {
            "name": self.name,
            "description": self.description,
            "files": list(self.files),
        }

    @property
    def files(self):
        for path in (self.local_repo / self.name).glob("**/*.*"):
            if not path.name.startswith('.'):
                urlpath = path.as_posix().replace(self.local_repo.as_posix(), "")
                yield {"path": urlpath[1:], "url": self.base_url + urlpath}


class DatasetCTA1DC(Dataset):
    name = "cta-1dc"
    description = "tbd"


class DatasetDarkMatter(Dataset):
    name = "dark_matter_spectra"
    description = "tbd"


class DatasetCatalogs(Dataset):
    name = "catalogs"
    description = "tbd"


class DatasetFermi2FHL(Dataset):
    name = "fermi_2fhl"
    description = "tbd"


class DatasetFermi3FHL(Dataset):
    name = "fermi_3fhl"
    description = "tbd"


class DatasetFermiSurvey(Dataset):
    name = "fermi_survey"
    description = "tbd"


class DatasetHESSDL3DR1(Dataset):
    name = "hess-dl3-dr1"
    description = "tbd"


class DatasetImages(Dataset):
    name = "images"
    description = "tbd"


class DatasetJointCrab(Dataset):
    name = "joint-crab"
    description = "tbd"


class DatasetEBL(Dataset):
    name = "ebl"
    description = "tbd"


class DatasetGammaCat(Dataset):
    name = "gamma-cat"
    description = "tbd"
    files = [
        {
            "path": "gamma-cat/gammacat.fits.gz",
            "url": "https://github.com/gammapy/gamma-cat/raw/master/output/gammacat.fits.gz"
        }
    ]


class DatasetFermiLat(Dataset):
    name = "fermi-lat-data"
    description = "tbd"
    files = [
        {
            "path": "fermi_3fhl/fermi_3fhl_events_selected.fits.gz",
            "url": "https://github.com/gammapy/gammapy-fermi-lat-data/raw/master/3fhl/allsky/fermi_3fhl_events_selected.fits.gz"
        },
        {
            "path": "fermi_3fhl/fermi_3fhl_exposure_cube_hpx.fits.gz",
            "url": "https://github.com/gammapy/gammapy-fermi-lat-data/raw/master/3fhl/allsky/fermi_3fhl_exposure_cube_hpx.fits.gz"
        },
        {
            "path": "fermi_3fhl/fermi_3fhl_psf_gc.fits.gz",
            "url": "https://github.com/gammapy/gammapy-fermi-lat-data/raw/master/3fhl/allsky/fermi_3fhl_psf_gc.fits.gz"
        },
        {
            "path": "fermi_3fhl/iso_P8R2_SOURCE_V6_v06.txt",
            "url": "https://github.com/gammapy/gammapy-fermi-lat-data/raw/master/isodiff/iso_P8R2_SOURCE_V6_v06.txt"
        }
    ]


class DatasetIndex:
    path = "download/data/gammapy-data-index.json"
    datasets = [
        DatasetCTA1DC,
        DatasetDarkMatter,
        DatasetCatalogs,
        DatasetFermi3FHL,
        DatasetFermi2FHL,
        DatasetFermiSurvey,
        DatasetHESSDL3DR1,
        DatasetImages,
        DatasetJointCrab,
        DatasetEBL,
        DatasetFermiLat,
        DatasetGammaCat,
    ]

    def make(self):
        records = list(self.make_records())
        txt = json.dumps(records, indent=True)
        log.info(f"Writing {self.path}")
        Path(self.path).write_text(txt)

    def make_records(self):
        for cls in self.datasets:
            yield cls().record


@click.group()
def cli():
    """Make the gammapy.org webpage."""
    logging.basicConfig(level="INFO")


@cli.command("all")
@click.pass_context
def cli_all(ctx):
    """Run all steps"""
    ctx.invoke(cli_dataset_index)


@cli.command("dataset-index")
def cli_dataset_index():
    """Generate data index file"""
    DatasetIndex().make()


if __name__ == "__main__":
    cli()
