export interface IUserProfile {
    email: string;
    is_active: boolean;
    is_superuser: boolean;
    first_name: string;
    last_name: string;
    gender: string;
    id: number;
}

export interface IUserProfileUpdate {
    email?: string;
    first_name?: string;
    last_name?: string;
    gender?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
}

export interface IUserProfileCreate {
    email: string;
    first_name?: string;
    last_name?: string;
    gender?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
}

export interface IUSurvey {
    id: number;
    title: string;
    description: string;
    create_at: string;
    active_survey: boolean;
    owner_id: number;
}

export interface IUSurveyCreate {
    title: string;
    description?: string;
    active_survey?: boolean;
    owner_id: number;
}

export interface IUSurveyUpdate {
    title?: string;
    description?: string;
    active_survey?: string;
}
