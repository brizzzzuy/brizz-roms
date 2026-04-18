"""
Idempotent seed of the Xiaomi 13 Lite device and the three HyperOS builds
ported from the @brezyck Telegram channel.

Safe to re-run: get_or_create keys each row, and builds are deduped by
(device, build_version).
"""
from datetime import date
from django.core.management.base import BaseCommand
from devices.models import Device, Build


DEVICE = {
    'codename': 'ziyi',
    'name': 'Xiaomi 13 Lite',
    'brand': 'Xiaomi',
    'maintainer': 'brizz',
    'latest_version': '3.0.7.0',
    'size': '~5 GB',
    'released_date': date(2023, 1, 31),
}

BUILDS = [
    {
        'build_version': '3.0',
        'android_version': '15',
        'build_type': 'Port',
        'size': '5 GB',
        'is_maintained': True,
        'release_date': date(2026, 1, 26),
        'download_link': 'https://drive.google.com/file/d/13uVEUol8FFDqkbBX_qB5Rues7omkcCYV/view?usp=sharing',
        'changelog_link': 'https://t.me/brezyck/107',
        'install_guide_link': 'https://t.me/brezyck/107',
    },
    {
        'build_version': '3.0.2.0',
        'android_version': '15',
        'build_type': 'Port',
        'size': '5 GB',
        'is_maintained': True,
        'release_date': date(2026, 3, 16),
        'download_link': 'https://drive.google.com/file/d/1iq781fCD7kDqX5ecKbx58jTEkN6tJhsL/view?usp=sharing',
        'changelog_link': 'https://t.me/brezyck/120',
        'install_guide_link': 'https://t.me/brezyck/120',
    },
    {
        'build_version': '3.0.7.0',
        'android_version': '16',
        'build_type': 'Port',
        'size': '5 GB',
        'is_maintained': True,
        'release_date': date(2026, 3, 18),
        'download_link': 'https://drive.google.com/file/d/1TmTkoHfBW6SLG0mwpZGARSNlwb66nVtf/view?usp=sharing',
        'changelog_link': 'https://t.me/brezyck/129',
        'install_guide_link': 'https://t.me/brezyck/129',
    },
]


class Command(BaseCommand):
    help = 'Seed Xiaomi 13 Lite and 3 HyperOS builds sourced from @brezyck'

    def handle(self, *args, **kwargs):
        device, created = Device.objects.get_or_create(
            codename=DEVICE['codename'],
            defaults=DEVICE,
        )
        if not created:
            # Keep metadata fresh without clobbering uploaded images.
            for k, v in DEVICE.items():
                setattr(device, k, v)
            device.save()
        self.stdout.write(self.style.SUCCESS(
            f"{'Created' if created else 'Updated'} device: {device.name} ({device.codename})"
        ))

        for b in BUILDS:
            build, bcreated = Build.objects.get_or_create(
                device=device,
                build_version=b['build_version'],
                defaults=b,
            )
            if not bcreated:
                for k, v in b.items():
                    setattr(build, k, v)
                build.save()
            self.stdout.write(self.style.SUCCESS(
                f"  {'+' if bcreated else '~'} Build {build.build_version} (Android {build.android_version})"
            ))
