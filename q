                                       Table "public.socialapp_profile"
    Column     |          Type          | Collation | Nullable |                    Default                    
---------------+------------------------+-----------+----------+-----------------------------------------------
 id            | integer                |           | not null | nextval('socialapp_profile_id_seq'::regclass)
 profile_photo | character varying(255) |           | not null | 
 bio           | text                   |           | not null | 
 user_id       | integer                |           | not null | 
 name          | character varying(120) |           | not null | 
Indexes:
    "socialapp_profile_pkey" PRIMARY KEY, btree (id)
    "socialapp_profile_user_id_key" UNIQUE CONSTRAINT, btree (user_id)
Foreign-key constraints:
    "socialapp_profile_user_id_b2ffc48a_fk_auth_user_id" FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED
Referenced by:
    TABLE "socialapp_comment" CONSTRAINT "socialapp_comment_user_id_24ce3e44_fk_socialapp_profile_id" FOREIGN KEY (user_id) REFERENCES socialapp_profile(id) DEFERRABLE INITIALLY DEFERRED
    TABLE "socialapp_image" CONSTRAINT "socialapp_image_user_id_05c2f779_fk_socialapp_profile_id" FOREIGN KEY (user_id) REFERENCES socialapp_profile(id) DEFERRABLE INITIALLY DEFERRED

