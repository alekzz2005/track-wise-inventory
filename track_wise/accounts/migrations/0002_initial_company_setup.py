from django.db import migrations, models
import django.db.models.deletion

def create_default_company(apps, schema_editor):
    Company = apps.get_model('accounts', 'Company')
    # Create a default company
    company = Company.objects.create(
        name='Default Company',
        address='Default company address',
        contact_info='Default contact information'
    )
    return company

def assign_default_company_to_profiles(apps, schema_editor):
    UserProfile = apps.get_model('accounts', 'UserProfile')
    Company = apps.get_model('accounts', 'Company')
    
    # Get the default company (should be ID=1 since we just created it)
    default_company = Company.objects.first()
    if not default_company:
        default_company = create_default_company(apps, schema_editor)
    
    # Assign company to all existing profiles
    for profile in UserProfile.objects.all():
        profile.company = default_company
        profile.save()

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        # First create the Company model
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField(blank=True)),
                ('contact_info', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        # Then add the company field to UserProfile, but nullable first
        migrations.AddField(
            model_name='userprofile',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.company'),
        ),
        # Run the function to create default company and assign it
        migrations.RunPython(create_default_company),
        migrations.RunPython(assign_default_company_to_profiles),
        # Finally make the company field non-nullable
        migrations.AlterField(
            model_name='userprofile',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.company'),
        ),
    ]