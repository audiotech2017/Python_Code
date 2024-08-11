SET
    IDENTITY_INSERT CJLR_NEWSP.DBO.AbpUsers OFF
INSERT INTO
    [dbo].[AbpUsers] (
        [AccessFailedCount],
        [AuthenticationSource],
        [ConcurrencyStamp],
        [CreationTime],
        [CreatorUserId],
        [DeleterUserId],
        [DeletionTime],
        [EmailAddress],
        [EmailConfirmationCode],
        [IsActive],
        [IsDeleted],
        [IsEmailConfirmed],
        [IsLockoutEnabled],
        [IsPhoneNumberConfirmed],
        [IsTwoFactorEnabled],
        [LastLoginTime],
        [LastModificationTime],
        [LastModifierUserId],
        [LockoutEndDateUtc],
        [Name],
        [NormalizedEmailAddress],
        [NormalizedUserName],
        [Password],
        [PasswordResetCode],
        [PhoneNumber],
        [ProfilePictureId],
        [SecurityStamp],
        [ShouldChangePasswordOnNextLogin],
        [Surname],
        [TenantId],
        [UserName],
        [SignInToken],
        [SignInTokenExpireTimeUtc],
        [GoogleAuthenticatorKey],
        [NameCn],
        [DepartmentCn],
        [DepartmentEn],
        [NameEn],
        [PositionCn],
        [PositionEn],
        [WorkNo],
        [PurcharseGroupId],
        [OrganizationId],
        [ReportTo1],
        [ReportTo2],
        [PositionCode],
        [DepartmentHead],
        [OldJobLevel]
    )
SELECT
    [AccessFailedCount],
    [AuthenticationSource],
    [ConcurrencyStamp],
    [CreationTime],
    [CreatorUserId],
    [DeleterUserId],
    [DeletionTime],
    [EmailAddress],
    [EmailConfirmationCode],
    [IsActive],
    [IsDeleted],
    [IsEmailConfirmed],
    [IsLockoutEnabled],
    [IsPhoneNumberConfirmed],
    [IsTwoFactorEnabled],
    [LastLoginTime],
    [LastModificationTime],
    [LastModifierUserId],
    [LockoutEndDateUtc],
    [Name],
    [NormalizedEmailAddress],
    [NormalizedUserName],
    [Password],
    [PasswordResetCode],
    [PhoneNumber],
    [ProfilePictureId],
    [SecurityStamp],
    [ShouldChangePasswordOnNextLogin],
    [Surname],
    [TenantId],
    [UserName],
    [SignInToken],
    [SignInTokenExpireTimeUtc],
    [GoogleAuthenticatorKey],
    [NameCn],
    [DepartmentCn],
    [DepartmentEn],
    [NameEn],
    [PositionCn],
    [PositionEn],
    [WorkNo],
    [PurcharseGroupId],
    [OrganizationId],
    [ReportTo1],
    [ReportTo2],
    [PositionCode],
    [DepartmentHead],
    [OldJobLevel]
FROM
    cjlr_Newsp2.dbo.abpusers
where
    PositionCode in ('10000420', '10002138')
SET
    IDENTITY_INSERT CJLR_NEWSP.DBO.AbpUsers ON